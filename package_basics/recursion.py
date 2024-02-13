def fibonacci(i):
    while i > -1:
        if i == 0:
            return 0
        if i == 1:
            return 1
        else:
            return fibonacci(i - 1) + fibonacci(i - 2)


n = int(input('enter iteration : '))
print(f'the fibonacci number of {n} iteration is {fibonacci(n)}')


def find_factorial(n):
    '''this programs helps to find factorial'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n - 1)


print(find_factorial(5))