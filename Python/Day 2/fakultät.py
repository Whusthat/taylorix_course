# printe die fakultät einer zahl aus einem input
base = int(input("Zahl eingeben : "))
i = 1
fakultaet = 1

while i <= base:
    fakultaet = fakultaet * i
    i = i + 1

print(f"{base}! = {fakultaet}")
