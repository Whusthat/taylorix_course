import sys
import mysql.connector
from tabulate import tabulate
from my_classes import RangeError
from passlib.hash import pbkdf2_sha256


def menu_loop():
    clipboard = []
    while True:
        print(f'1) Adresse eingeben')
        print(f'2) Adresse speichern')
        print(f'3) Adresse laden')
        print(f'4) Adresse anzeigen')
        print(f'5) Adresse löschen')
        print(f'6) Adresse suchen')
        print(f'7) schließen')
        choice = validate_input(True)
        if choice == 1:
            clipboard.append(get_user_input())
        elif choice == 2:
            save_to_db(clipboard)
            clipboard.clear()
        elif choice == 3:
            clipboard = load_db_data()
        elif choice == 4:
            print_data(clipboard)
        elif choice == 5:
            delete_record()
            clipboard.clear()
        elif choice == 6:
            search()
        elif choice == 7:
            close()


def create_db_object():
    db = mysql.connector.connect(host='localhost', user='root', password='', database='adressverwaltung')
    return db


def save_to_db(liste):
    db = create_db_object()
    for adresse in liste:
        sql_statement = "INSERT INTO adresse (vorname, nachname, strasse, ort, plz) VALUES (%s, %s, %s, %s, %s)"
        values = (adresse[0], adresse[1], adresse[2], adresse[3], adresse[4])
        cursor = db.cursor()
        cursor.execute(sql_statement, values)
        db.commit()


def load_db_data():
    db = create_db_object()
    cursor = db.cursor()
    cursor.execute('SELECT vorname, nachname, strasse, ort, plz FROM adresse')
    result = cursor.fetchall()
    db.close()
    return result


def print_data(liste):
    print(tabulate(liste, headers=['Vorname', 'Nachname', 'Strasse', 'Ort', 'Postleitzahl'], tablefmt='pretty'))


def delete_record():
    db = create_db_object()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM adresse ORDER BY a_id')
    result = cursor.fetchall()
    record_list = result
    print(tabulate(record_list, headers=[
        'a_id',
        'Vorname',
        'Nachname',
        'Strasse',
        'Ort',
        'Postleitzahl'
    ], tablefmt='pretty'))

    try:
        a_id = int(input(f'Bitte geben sie die a_id der Adresse an welche sie löschen möchten : '))
        exists = False
        for records in record_list:
            if a_id in records:
                exists = True
        if exists:
            cursor.execute(f'DELETE FROM adresse WHERE a_id = {a_id}')
            db.commit()
        else:
            raise RangeError
    except ValueError:
        print(f'Bei ihrer eingabe handelt es sicht nicht um eine Zahl')

    except RangeError:
        print(f'Zu ihrer Eingabe existiert keine passende Adresse')


def get_user_input():
    vorname = input(f'Bitte Vorname eingeben : ')
    nachname = input(f'Bitte Nachname eingeben : ')
    strasse = input(f"Bitte Strasse eingeben : ")
    ort = input(f'Bitte Ort eingeben : ')
    plz = input(f'Bitte Plz eingeben : ')

    return tuple((vorname, nachname, strasse, ort, plz))


def validate_input(logged_in=False):
    try:
        text = 'Wähle Menu Punkt 1-5 : ' if logged_in else '1) Login\n2) Sign Up\n-> '
        x = int(input(f'{text}'))
        if x < 0 or x > 7 and logged_in:
            raise ValueError()
        elif x < 0 or x > 2 and not logged_in:
            raise ValueError()
        else:
            return x
    except ValueError:
        print(f'Fehler Zahl zu groß/klein oder keine Zahl')
        validate_input()


def search():
    search_phrase = input(f'Geben sie einen Begriff zur Suche ein : ')

    db = create_db_object()
    cursor = db.cursor()
    cursor.execute(f'SELECT vorname, nachname, strasse, ort, plz FROM adresse WHERE vorname LIKE "%{search_phrase}%"'
                   f'OR nachname LIKE "%{search_phrase}%"'
                   f'OR strasse LIKE "%{search_phrase}%"'
                   f'OR ort LIKE "%{search_phrase}%"'
                   f'OR plz LIKE "%{search_phrase}%"')
    result = cursor.fetchall()
    db.close()
    print_data(result)


def close():
    sys.exit()


def log_in():
    # grab input from user
    choice = validate_input()
    # get db oject
    db = create_db_object()
    # create cursor
    cursor = db.cursor()
    # if choice 1 == login
    if choice == 1:
        # grab user name
        user = input(f"Bitte geben sie ihren Usernamen an : ")
        # grab user password
        pw = input(f"Bitte geben sie Pw ein : ")
        # salt is username
        salt = str.encode(user)
        # hash user password + Salt
        pwhash = pbkdf2_sha256.hash(pw, salt=salt)
        # execute SQL statement -> wo user == input user
        cursor.execute(f"SELECT user, pw, fehlversuch, aktiv FROM users WHERE user LIKE '{user}';")
        try:
            # grab result from sql statement
            result = cursor.fetchall()
            # declare user name
            user_name = result[0][0]
            # declare pw
            user_pw = result[0][1]
            # declare "fehlversuch"
            fehlversuch = result[0][2]
            # declare aktiv status
            aktiv_flag = result[0][3]
            # check if account is aktiv
            if aktiv_flag == 'inaktiv':
                print('Der Account ist gesperrt')
                log_in()
            else:
                # check if result correct data
                if len(result) > 0 and result[0][0] == user:
                    # check if pw hashes are matching
                    if user_pw == pwhash:
                        # after successful login set fehlversuch to 0
                        cursor.execute(f"UPDATE users SET fehlversuch = {0} WHERE user LIKE '{user_name}'")
                        db.commit()
                        menu_loop()
                    # if password is wrong increase fehlversuch by 1
                    else:
                        # if fehlversuch is > 4 we flag the account to inaktiv
                        if fehlversuch > 4:
                            print(f'Zu viele Fehlerhafte Login Versuche ihr Account ist gesperrt!')
                            cursor.execute(f"UPDATE users SET aktiv = 'inaktiv' WHERE user LIKE '{user_name}'")
                        print('Das Passwort stimmt nicht mit dem Username überein')
                        cursor.execute(f"UPDATE users SET fehlversuch "
                                       f"= '{fehlversuch+1}' WHERE user LIKE '{user_name}'")
                        db.commit()
                        log_in()
                else:
                    raise Exception
        except (mysql.connector.Error, IndexError):
            print('Dieser User existiert nicht')
            log_in()

        else:
            db.commit()
    # choice == 2 -> create user
    else:
        print('Please fill out username and passwort to SignUp')
        user = input(f"Please enter you E-Mail address : ")
        # check if username exists
        exists = check_duplicate_users(user)
        pw = input(f"Please enter a strong passwort : ")
        salt = str.encode(user)
        hash_pw = pbkdf2_sha256.hash(pw, salt=salt)
        # username does not exists create new user
        if exists:
            create_new_user(user, hash_pw)
            log_in()
        else:
            # if username exists give a second prompt to for username
            user = input(f"This name is already taken try another one : ")
            exists = check_duplicate_users(user)
            if exists:
                create_new_user(user, hash_pw)
                log_in()
            else:
                log_in()
    db.close()


def create_new_user(user, pw):
    db = create_db_object()
    cursor = db.cursor()
    cursor.execute(f'INSERT INTO users (user, pw, fehlversuch, aktiv) VALUES ("{user}", "{pw}", "{0}", "{"aktiv"}")')
    db.commit()


def check_duplicate_users(user_name):
    db = create_db_object()
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM users WHERE user LIKE "{user_name}"')
    result = cursor.fetchall()

    if len(result) > 0:
        db.close()
        return False
    else:
        db.close()
        return True


def main():
    log_in()


if __name__ == '__main__':
    main()
