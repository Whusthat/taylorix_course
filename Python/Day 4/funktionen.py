# step - 1
# without function

name = 'Scholl'
print('Hallo - mein name ist', name)
name = 'Peter'
print('Hallo - mein name ist', name)
name = 'Klaus'
print('Hallo - mein name ist', name)

# step - 2
# define function
# as you can see no name is given as argument for the function


def gruss():
    print('Hallo - mein name ist')


# Step - 3
# declare parameter name to pass to the function

def gruss_with_parameter(name):
    print(f'Hallo - mein name ist {name}')


gruss()
gruss_with_parameter('Klaus')