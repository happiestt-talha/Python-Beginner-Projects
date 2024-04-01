def fib(lim):
    a, b = 0, 1
    while a < lim:
        yield a
        a, b = b, a + b


# fib(9)
# print(*(next(i) for i in fib(6)))
print(type(fib(6)))
