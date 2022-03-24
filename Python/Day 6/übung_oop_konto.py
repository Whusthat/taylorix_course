from random import randint
from cls import cls

"""
Class Konto {Abstract} -> Attributes (name, inhaber, kontostand) | Methoden (anzeigen_stand(), einzahlen())
Sub-Class Giro -> Attributes (rahmen) | Methoden (einzahlen())
Sub-Class Guthaben -> Attributes () | Methoden (einzahlen())  
"""


class Konto:

    def __init__(self, kontoinhaber):
        self.inhaber = kontoinhaber
        self.kontostand = 0
        self.nummer = self.generiere_kontonummer()

    def generiere_kontonummer(self):
        nr = ''
        for i in range(6):
            n = randint(0, 9)
            nr += str(n)
        return nr

    def anzeigen(self):
        print(f'Ihr Konto: {self.nummer} hat den aktuellen Kontostand von {self.kontostand}€')

    def einzahlen(self, betrag):
        self.kontostand += betrag
        print(f'Ihrem Konto wurde {betrag}€ zugewiesen')
        self.anzeigen()


class Guthabenkonto(Konto):

    def auzahlen(self, betrag):
        if self.kontostand < betrag:
            print(f'Konto nicht ausreichend gedeckt')
        else:
            self.kontostand -= betrag
            print(f'Ihrem Konto wurde {betrag}€ abgezogen')


class Girokonto(Konto):

    def __init__(self, kontoinhaber):
        self.rahmen = int(input(f'Kontorahmen eingeben : '))
        # or super().__init__(kontoinhaber)
        Konto.__init__(self, kontoinhaber)

    def auzahlen(self, betrag):
        if (self.kontostand + self.rahmen) < betrag:
            print(f'Konto nicht ausreichend gedeckt')
        else:
            self.kontostand -= betrag


def main():
    konto1 = Girokonto('Sebastian Müller')
    konto1.anzeigen()
    konto1.einzahlen(200)
    konto1.auzahlen(500)

    konto2 = Guthabenkonto('Peter Zwegat')
    konto2.anzeigen()


main()
