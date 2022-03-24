# initialized by list((value1, value2)) or '[value1, value2]'
my_list = list(('Apfel', 'Birne', 'Banane'))

# tuples will not let you assign new values initialized by the '(value1, value2)'
my_tuple = (1, 2, 3)

# set uses no index you can not access the single values initialized by the '{value1, value2}',
# no duplicate values allowed
my_set = {'apfel', 'birne'}

# list with key as index initialized by '{key: value, ...}'
my_dictonary = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}

# you can alter dictonarys
dictonary = {'key': 'value'}

# adding key 'neu' with value 'new value'
dictonary['neu'] = 'new value'


print(my_list)              # ['Apfel', 'Birne', 'Banane']
print(my_tuple)             # (1, 2, 3)
print(my_set)               # {'birne', 'apfel'}
print(my_dictonary)         # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(dictonary['key'])     # value
print(dictonary['neu'])     # new value


