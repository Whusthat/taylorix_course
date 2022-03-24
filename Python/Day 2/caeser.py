# handles bool input
def get_bool() -> str:
    x = ""
    while x != "e" and x != "d":
        x = input(f"Enter 'e' for encryption or 'd' for decryption : ").lower()

    return x


# handles int input
def get_int() -> int:

    x = input("Zahl eingeben : ")
    formatted_string = ''

    for char in x:

        o = ord(char)

        # ASCII 0-9
        if 48 <= o <= 57:
            formatted_string = formatted_string + char

    return int(formatted_string) if len(formatted_string) > 0 else get_int()


# handles string input
def format_string(string) -> str:
    x = string.upper()
    formatted_string = ''

    for char in x:

        o = ord(char)
        # ASCII A-Z
        if 65 <= o <= 90:
            formatted_string = formatted_string + char

    return formatted_string


def cipher(key, string, method) -> str:

    store_key = key

    x = format_string(string)
    z = ""

    if key % 26 == 0:
        return f"Key ungültig \nkey = 0 \noutput = {x} (identisch zum input {x})"

    # macht aus negativen int einen positiven
    key = abs(key)

    # reverse key für decrypten
    if method == "d":
        key = key * (-1)

    for char in x:

        # key % 26 erlaubt keys > 52
        o = ord(char) + (key % 26)

        if o > 90:
            o = o - 26
        if o < 65:
            o = o + 26
        z = z + chr(o)

    return f"Der {'encrypted' if method == 'e' else 'decrpyted'} String ist {z} mit dem key {store_key}"


print(cipher(get_int(), input(f"Type Text to encrypt/decrypt : "), get_bool()))
