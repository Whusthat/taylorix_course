# r = read - error if file not exits
# a = append - open file to append - if file not exists : create - appends on content
# w = write - opens file to write - if not exists : create - overriedes content !!! dangerous
# x = create

# with syntax automaticly closes file

# with open('C:/Users/s.müller/Desktop/ausgabe/readme.txt', 'a') as f:
#    f.write('Hallo')


# read = whole file
# readline = reads 1 line
# readlines = reads all lines return a list of lines

with open('C:/Users/s.müller/Desktop/ausgabe/readme.txt', 'r') as f:
    text = f.read()
