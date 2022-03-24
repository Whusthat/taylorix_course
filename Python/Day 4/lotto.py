from random import randint


def cls():
    for i in range(1, 50):
        print()


def count_all_numbers(list):

    dictonary = {}
    text = list
    # loop over every char in string
    for r in list:
        for char in r:
            # set key = value
            key = char
            # if key exists increase value + 1
            if key in dictonary:
                dictonary[key] += 1
            # if key does not exist set value = 1
            else:
                dictonary[key] = 1

    sorted_dict = dict(sorted(dictonary.items(), key=lambda item: item[0]))
    return sorted_dict


def lotto():
    # do a screen clear
    cls()
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


def output(dict):
    for key in sorted(dict):
        print(f"Die Zahl : '{key}' is {dict[key]} vorgekommen")


numbers = lotto()
dictonary = count_all_numbers(numbers)

print(f"Lotto zahlen : {numbers}")
output(count_all_numbers(numbers))




