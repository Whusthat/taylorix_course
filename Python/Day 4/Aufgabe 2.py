from random import randint


def get_input():
    player_tip = []
    i = 0
    while i < 6:

        number = int(input(f"Bitte Geben sie die {i + 1}. Zahl ein : "))
        if number in player_tip:
            continue
        player_tip.append(number)
        i = i + 1
    return player_tip


def lotto():
    # keep track of all numbers that where valid and drawn
    valid_numbers = []
    # counter for defining a set
    i = 0
    # amount of draw's
    ziehungen = 2

    while ziehungen > 0:
        list2 = []
        while i < 6:

            draw = randint(1, 49)

            if draw in valid_numbers:
                continue
            list2.append(draw)
            i = i + 1

        valid_numbers.append(list(list2))
        ziehungen = ziehungen - 1

        i = 0

    return valid_numbers


def compare():
    ziehungen = lotto()
    player = get_input()

    for ziehung in ziehungen:
        for n in player:
            if n in ziehung:
                print('test')


compare()