# Nach wie viel Jahren sterben die Mäuse aus
def mouse_dead_when():
    jung = 2000
    erwachsene = 0
    alt = 0
    jahr = 0

    while (int(jung) + int(erwachsene) + int(alt)) > 0:
        alt = erwachsene
        erwachsene = jung
        jung = erwachsene / 2
        jahr += 1

    return jahr


print(f"Die mäuse sterben nach {mouse_dead_when()} Jahren")


# Mäuse Population nach x Jahren
def mouse_count():
    jung = 10000
    erwachsene = 0
    alt = 0
    jahre = 10

    while jahre > 0:
        alt = erwachsene
        erwachsene = jung
        jung = erwachsene / 2
        jahre -= 1

    return round(jung), round(erwachsene), round(alt)


print(f"Population: {sum(mouse_count())}")