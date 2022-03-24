def sum(n):
    if n == 1:
        return n
    return n + sum(n - 1)


def quer(n):
    if n < 10:
        return n
    return quer(n // 10) + n % 10


def fak(n):
    if n == 1:
        return n
    return n * fak(n - 1)


def hanoi(n, start, ziel, hilfe):
    if n == 1:
        print("Move disk 1 from source", start, "to destination", ziel)
        return
    hanoi(n - 1, start, hilfe, ziel)
    print("Move disk", n, "from source", start, "to destination", ziel)
    hanoi(n - 1, hilfe, ziel, start)


def main():
    print(f'Die Summe der Zahlen von n-n : {sum(10)}')
    print(f'Die Quersumme der Zahl n : {quer(454646)}')
    print(f'Die Fakultät der Zahl n : {fak(5)}')

    # Driver code
    n = 4
    hanoi(n, 'A', 'B', 'C')


if __name__ == '__main__':
    main()