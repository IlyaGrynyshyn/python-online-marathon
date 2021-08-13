def divisor(number):
    for x in range(1, number + 1):
        if number / x == int(number / x):
            yield x
    while True:
        yield None

three = divisor(3)
print(next(three))
print(next(three))
print(next(three))
