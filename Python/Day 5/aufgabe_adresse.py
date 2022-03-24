import sys


def menu_loop():
    path_to_file = 'C:/Users/s.müller/Desktop/ausgabe/readme.txt'
    menu_active = True
    ram = []


    while menu_active:
        print(f'1) Adresse eingeben')
        print(f'2) Adresse speichern')
        print(f'3) Adresse laden')
        print(f'4) Adresse anzeigen')
        print(f'5) schließen')
        choose = validate_input()
        if choose == 1:
            ram.append(get_input())
        elif choose == 2:
            save_to_file(ram, path_to_file)
        elif choose == 3:
            ram = load_file(path_to_file) + ram
        elif choose == 4:
            print_file_content(ram)
        elif choose == 5:
            close()


def get_input():
    name = input(f'Bitte Namen eingeben : ')
    vorname = input(f'Bitte Vornamen eingeben : ')
    ort = input(f'Bitte Ort eingeben : ')

    return f'{name} | {vorname} | {ort} | '


def save_to_file(liste, path):
    with open(path, "w") as f:
        for line in liste:
            f.write(line + '\n')


def load_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        stack = []
        for s in lines:
            stack.append(s)
    return stack


def print_file_content(liste):
    if len(liste) != 0:
        print(f'-----------------------------------------------------')
        for list in liste:
            print(list)
        print(f'-----------------------------------------------------')
    else:
        print(f'Keine adressen vorhanden')


def close():
    sys.exit()


def validate_input():
    try:
        x = int(input(f'Wähle Menu Punkt - 1-5 : '))
        if x < 0 or x > 5:
            raise Exception()
        return x
    except ValueError:
        print(f'Fehler Zahl zu groß/klein oder keine Zahl')
        validate_input()


menu_loop()