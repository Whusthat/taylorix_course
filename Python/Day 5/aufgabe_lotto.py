from random import randint


def get_input():
    player_tip = []
    i = 0
    set_size = 6

    while i < set_size:
        try:
            number = int(input(f"Bitte geben sie die {i + 1}. Zahl ein (1-49): "))
            # check for duplicates
            if number in player_tip:
                print(f"'{number}' already picked! Your current Tips: {player_tip}! Try another number")
                continue
            # check for range 1-49
            if number > 49 or number < 1:
                print('Number out of range make sure to enter only (1-49)')
                continue
            player_tip.append(number)
            i = i + 1
        except ValueError:
            print('Please enter a number!')

    return player_tip


def get_ziehungen():
    while True:
        try:
            number = int(input(f"Bitte geben sie die anzahl der Ziehungen ein : "))
            return number
        except ValueError:
            print('Please enter a number!')


def lotto():
    # keep track of all numbers that where valid and drawn
    valid_numbers = []
    # counter for defining a set
    i = 0
    # amount of draw's
    ziehungen = get_ziehungen()

    while ziehungen > 0:
        list2 = []
        while i < 6:
            draw = randint(1, 49)
            if draw in list2:
                continue
            list2.append(draw)
            i = i + 1
        valid_numbers.append(list(list2))
        ziehungen = ziehungen - 1
        i = 0
    return valid_numbers


def compare(ziehungen, player):
    winners = []

    for ziehung in ziehungen:
        # wrap the element in list for the winners in each "ziehung"
        wrapper = []
        for n in player:
            if n in ziehung:
                wrapper.append(n)
        winners.append(wrapper)
    return winners, ziehungen, player


def output(winners, ziehungen, player):
    w = winners
    z = ziehungen
    p = player
    i = 0
    money_rain = []
    dictonary = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    while i < len(z):
        if len(w[i]) >= 0:
            dictonary[len(w[i])] = dictonary[len(w[i])] + 1
        if len(w[i]) == 6:
            money_rain.append([z[i], z.index(z[i])+1])
        i = i + 1

    for key, value in sorted(dictonary.items()):
        if key > 2:
            print(f"{key} Richtige: {value}x")
            if key == 6 and len(money_rain) > 0:
                print(money_rain)


def main():
    winners, ziehungen, player = compare(lotto(), get_input())
    output(winners, ziehungen, player)


main()
