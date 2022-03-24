# print 1x1, 1x2, 1x3 ...
i = 1

while i < 11:
    j = 1
    while j < 11:
        print(f"{i} * {j} = {i * j}")
        j = j + 1
    i = i + 1

