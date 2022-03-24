from random import randint


def cls():
    for i in range(1, 50):
        print()


def count_unique(list) -> dict:

    dictonary = {}

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

    # key parameter in sorted determines the element we sort for
    sorted_dict = (sorted(dictonary.items(), key=lambda item: item[0]))
    return sorted_dict


def count_chars(text) -> dict:
    dictonary = {}

    # loop over every char in string
    for char in text:
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


def count_eyes(list):
    summe = []

    for i in list:
        summe.append(sum(i))
    return count_chars(summe)


def wuerfel() -> list:
    # keep track of all numbers that where valid and drawn
    valid_numbers = []
    # counter for defining a set
    i = 0
    # amount of draw's
    wuerfe = int(input(f"Wie viele würfe soll es geben : "))
    anzahl_wuerfel = int(input("Mit wie vielen Würfeln soll gewürfelt werden : "))

    while wuerfe > 0:
        list2 = []
        while i < anzahl_wuerfel:

            draw = randint(1, 6)
            list2.append(draw)
            i = i + 1

        valid_numbers.append(list(list2))
        wuerfe = wuerfe - 1

        i = 0

    return valid_numbers


def output(dictonary):
    for key, value in dictonary.items():
        print(f"({key} : {value}x)")


list_of_numbers = wuerfel()
dictonary_of_numbers_sorted = count_unique(list_of_numbers)
output(count_eyes(list_of_numbers))
