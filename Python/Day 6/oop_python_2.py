class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f'Hallo, Leute mein {self.name} und bin {self.age} Alt')


class Pupils(Person):
    def write(self):
        return 'Der Schüler schreibt'


pers1 = Person('Peter', 22)
pers2 = Person('Axel', 18)
# create an instance of Pupils
pupil1 = Pupils('Seb', 40)

print(pupil1.write(), 'und ist', pupil1.age)
