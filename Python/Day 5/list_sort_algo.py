from random import randint


def sort(liste):

    w = liste
    # create stack for 3 corner exchange
    stack = []
    sorted = True

    # same as 'sorted == True'
    while sorted:
        sorted = False
        # -1 to not produce out of range
        for i in range(0, len(w)-1):
            # if current item is greater than next item switch indexes
            if w[i] > w[i+1]:
                stack = w[i+1]
                w[i+1] = w[i]
                w[i] = stack
                sorted = True

    return w


def main():
    # generate 20 random numbers between 1-100 with list comprehension
    x = [randint(1, 100) for x in range(20)]
    # keep the old list
    y = x.copy()
    sorted = sort(x)
    print(f"The unsorted List: {y} \nThe sorted List {sorted}")


main()