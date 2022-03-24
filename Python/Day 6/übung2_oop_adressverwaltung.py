"""
Adresse (Attribute | name, ort) (Methoden | ausgeben(), eingeben())
Adressliste (Attribute | liste von Adressen ) (Methoden | Adressliste_anzeigen())
"""


class Adresse:
    def __init__(self):
        self.name = input(f"Name eingeben : ")
        self.ort = input(f"Ort eingeben : ")

    def ausgeben(self):
        print(f"{self.name}, aus {self.ort}")


class Adressliste:
    def __init__(self):
        self.liste = []

    def anzeigen(self):
        for item in self.liste:
            item.ausgeben()

    def hinzufuegen(self, adr):
        self.liste.append(adr)


def main():
    a = Adresse()
    alist = Adressliste()
    alist.hinzufuegen(a)

    b = Adresse()
    alist.hinzufuegen(b)
    alist.anzeigen()

    alist.hinzufuegen(Adresse())
    alist.anzeigen()

    alist.anzeigen()


main()