import os


def check(file):
    with open(file, "r") as f:
        text = f.read()
        if text.upper() == "X":
            print(file)


def suche_in_ordner(ordner_pfad):
    file_list = []
    dir_list = []
    for file in os.listdir(ordner_pfad):
        if os.path.isdir(ordner_pfad + "/" + file):
            dir_list.append(ordner_pfad + "/" + file)
        else:
            file_list.append(ordner_pfad + "/" + file)
    if len(file_list) > 0:
        for file in file_list:
            check(file)
    if len(dir_list) > 0:
        for directory in dir_list:
            suche_in_ordner(directory)


suche_in_ordner("C:/test")