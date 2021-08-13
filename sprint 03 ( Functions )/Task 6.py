import random


def randomWord(args):
    if not args: yield None
    yield random.choice(args)
    yield from randomWord(args)


list = []

books = randomWord(list)
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))
print(next(books))

