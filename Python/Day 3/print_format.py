import datetime

# fstrings - datetime.now -> returns current date
print(f"{datetime.datetime.now():%d-%m-%Y}")


# format method on string
jahr = 2020
monat = "Februar"
tag = 28
us = "-"
de = "."

datum = "Das datum ist der {0}{3}{1}{3}{2}"
print(datum.format(tag, monat, jahr, de))
print(datum.format(tag, monat, jahr, us))

# third way - only works with tuple
person = ('John', 'Doe', 23, 'USA')
text = '%s %s is %s years old and lives in %s'

print(text %person)
