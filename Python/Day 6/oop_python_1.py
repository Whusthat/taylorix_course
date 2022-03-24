class MyClass:
    # the constructor for the class
    def __init__(self, name, age):
        self.name = name
        self.age = age


# calling an instance of the class MyClass
object = MyClass('Peter', 22)

# print(f'Mein name ist {object.name} \nund ich bin {object.age} Jahre alt')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'Hallo, Leute mein {self.name} und bin {self.age} Alt')


pers1 = Person('Peter', 22)
pers2 = Person('Axel', 18)

# delete a attribute of an object
# code: del pers2.age | del objectName.attribute

# add a new attribute to an object
# code: pers2.wir = 'hi' | objectName.attribute = value

print(f'Mein name ist {pers1.name} \nund ich bin {pers1.age} Jahre alt')
print(f'Mein name ist {pers2.name} \nund ich bin {pers2.age} Jahre alt')

