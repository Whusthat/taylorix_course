text = "Dies ist ein Text"

print(text[9:11])
# -1 gibt an das er von rechts nach links geht
print(text[2:0:-1])
# :: von start bis ende des strings
print(text[::-1])

string_reverse = ""

for x in text:
    string_reverse = x + string_reverse

print(string_reverse)

# ord returns ASCII decimal value
print(ord("A"))
# chr returns ASCII sign
print(chr(65))