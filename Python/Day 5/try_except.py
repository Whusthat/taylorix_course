# no error type passed = all types
# NameError = reference a variable who is not assigned
# ZeroDivisonError = Division by 0 not possilbe
# ValueError =

try:
    print('Es hatt geklappt')
    #print(x)
    #print(5/0)
    #int(input(f'Zahl eingeben : '))

except NameError:
    print(f'Eine {NameError} Fehler ist aufgetreten')

except ZeroDivisionError:
    print(f'Ein sonstiger Fehler')

except ValueError:
    print(f'Not a Number')


# validate input

def prompt():
    try:
        x = int(input('Zahl eingeben : '))
        if x < 0 or x > 49:
            raise Exception()
    except:
        print(f'Not a Number')
        prompt()


def main():
    prompt()


main()



list1 = [1,2,3]
list2 = []

print(list1+list2)