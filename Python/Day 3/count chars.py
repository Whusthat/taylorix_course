# function just removes every none alphabetic char
def format_string(string) -> str:
    x = string.upper()
    formatted_string = ''

    for char in x:
        o = ord(char)
        # ASCII A-Z
        if 65 <= o <= 90:
            formatted_string = formatted_string + char

    return formatted_string


def count_chars() -> dict:
    text = format_string(input(f'Enter a string : '))
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

    return dictonary


counted_chars = count_chars()

# print key+value
for chars in sorted(counted_chars.items()):
    print(chars)
