def fact(n):
    """ calculate n! interatively"""
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
        return result


def factorial(n):
    # n! can also be defined as n * (n-1)
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    """f(n) = f(n -1) + f(n -2)"""
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result


for i in range(32):
    print(i, fib(i), "\t", fibonacci(i))
# these don't return the same thing, the first one returns 'none' for the first two results