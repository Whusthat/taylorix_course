# Bilde die Summe aus n Zahlen

def count_n_numbers():
    # Frage nach Zahl als n
    n = int(input("gib zahl ein : "))
    sum = 0

    # loop über range 1-n
    for i in range(1, n + 1):
        print(f"{sum} + {i} = {sum + i} ")
        sum += i
    return sum


print(f"Die Summe der N-Zahlen ist: {count_n_numbers()}")