from sys import exit


def cls():
    for i in range(1, 50):
        print()


def wasauchimmer():
    cls()
    print('Dies ist die Funktion "wasauchimmer"')
    input('Weiter mit Return')
    return


def etwasanderes():
    cls()
    print('Dies ist die Funktion "etwasanderes"')
    input('Weiter mit Return')
    return


while True:

    cls()
    print('Bitte wählen: ')
    print(f'1.) wasauchimmer')
    print(f'2.) etwasanderes')
    print(f'x.) ENDE')
    choice = input(f'\nWähle Menu Punkt : ')

    if choice == "1":
        wasauchimmer()
    if choice == "2":
        etwasanderes()
    if choice == 'x':
        exit()