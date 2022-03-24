# recursive
def fib_1(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fib_1(n - 1) + fib_1(n - 2)


# iterative
def fib_2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# triangle swap without temp var
def triangle_swap():
    a = 7
    b = 2
    a = a + b
    b = a - b
    a = a - b
    return a, b


def main():
    print(fib_1(7))
    print(fib_2(250))
    print(triangle_swap())


if __name__ == '__main__':
    main()