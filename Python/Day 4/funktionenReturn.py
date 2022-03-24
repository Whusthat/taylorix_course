# write function with return
def addiere(a, b):
    return a + b


print(addiere(2, 3))


# return multiple values
def berechne(a, b):
    umfang = 2 * (a+b)
    flaeche = a * b
    return umfang, flaeche


u, f = berechne(3, 4)
print(f'Fläche : {f}')
print(f'Umfang : {u}')
print(berechne(3, 4))

