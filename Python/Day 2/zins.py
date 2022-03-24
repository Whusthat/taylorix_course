geldbetrag = int(input("Betrag Eingeben : "))
zinssatz = int(input("Zinssatz Eingeben : "))
jahre = int(input("Anzahl Zinsen : "))

# alternativ ein while loop mit einem counter { i = 1 | while i <= jahre }
for jahr in range(1, jahre+1):
    geldbetrag = round(float(geldbetrag + (geldbetrag * zinssatz / 100)))
    print(f"Jahr {jahr} - Betrag {geldbetrag}")
