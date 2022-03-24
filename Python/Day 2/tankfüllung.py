tank = float(input("Wie groß ist Tankfüllung : "))
verbrauch = float(input("Wie hoch ist der Verbrauch pro 100km : "))

print(round(tank*100 / verbrauch, 2))