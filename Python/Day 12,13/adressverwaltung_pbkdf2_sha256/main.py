import mysql.connector
from tkinter import *
from db_config import mysql_data
from passlib.hash import pbkdf2_sha512


class App:
    def __init__(self):
        root.geometry('400x150')
        root.title('Adressverwaltung')
        self.log_status = False
        self.login = LoginMask()
        root.mainloop()


class LoginMask:
    def __init__(self):
        self.login_mask = Frame(root, padx=10, pady=10, width=400, height=150)
        self.login_mask.pack(side=TOP, expand=YES)

        self.user_name_entry = Entry(self.login_mask)
        self.user_name_label = Label(self.login_mask, text='Username: ')
        self.user_name_entry.grid(row=0, column=1)
        self.user_name_label.grid(row=0, column=0)

        self.user_pw_entry = Entry(self.login_mask, show='*')
        self.user_pw_label = Label(self.login_mask, text='UserPw: ')
        self.user_pw_label.grid(row=1, column=0)
        self.user_pw_entry.grid(row=1, column=1)

        self.system_message = Label(self.login_mask, text='')
        self.system_message.grid(row=2, column=1)

        self.submit_button = Button(self.login_mask, text='SignIn', command=self.signIn)
        self.submit_button.grid(row=3, column=0, pady=10)

        self.submit_button = Button(self.login_mask, text='SignUp', command=self.signUp)
        self.submit_button.grid(row=3, column=1, pady=10)

    def signUp(self):
        username = self.user_name_entry.get()
        pwd = self.user_pw_entry.get()
        # salt is username
        salt = str.encode(username)
        # hash user password + Salt
        hashed_pw = pbkdf2_sha512.hash(pwd, salt=salt)
        db = Credentials()
        user_exists = db.get_resultset(f'SELECT * FROM users WHERE user LIKE "{username}"')
        if len(user_exists) > 0:
            self.system_message.configure(text='Dieser Name ist bereits vergeben!')
        else:
            db.execute_statement(f'INSERT INTO users '
                                 f'(user, pw, fehlversuch, aktiv) '
                                 f'VALUES ("{username}", "{hashed_pw}", "{0}", "{"aktiv"}")')
            self.system_message.configure(text="Nutzer angelegt!")

    def signIn(self):
        username = str(self.user_name_entry.get())
        pwd = str(self.user_pw_entry.get())
        # salt is username
        salt = str.encode(username)
        # hash user password + Salt
        hashed_pw = pbkdf2_sha512.hash(pwd, salt=salt)
        db = Credentials()
        result = db.get_resultset(f'SELECT user, pw, fehlversuch, aktiv FROM users WHERE user LIKE "{username}"')
        try:
            user_name = result[0][0]
            user_pw = result[0][1]
            user_attemps = result[0][2]
            user_active = result[0][3]
            if len(result) > 0:
                if user_pw == hashed_pw and user_active == 'aktiv':
                    print('looged in')
                else:
                    if user_attemps >= 3:
                        db.execute_statement(f'UPDATE users set aktiv = "inaktiv" WHERE user LIKE "{user_name}"')
                        self.system_message.configure(text="Account Gesperrt, wenden sie sich an ihren Admin")
                    else:
                        db.execute_statement(f'UPDATE users set '
                                             f'fehlversuch = {user_attemps+1} WHERE user LIKE "{user_name}"')
                        self.system_message.configure(text="Das Passwort zu dem"
                                                           " angebenen Username stimmt nicht überein")
            else:
                self.system_message.configure(text="Die Kombination aus Passwort und Nutzername"
                                                   " stimmt zu keinem Account überein")
        except IndexError:
            self.system_message.configure(text="Es kann keine Verbindung zur Datenbank hergestellt werden")


class DatabaseInterface:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=mysql_data["host"],
            user=mysql_data["user"],
            password=mysql_data["password"],
            database=mysql_data["database"]
        )


class Credentials(DatabaseInterface):

    def get_resultset(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        resultset = cursor.fetchall()
        self.connection.commit()
        return resultset

    def execute_statement(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()


if __name__ == '__main__':
    root = Tk()
    main = App()

