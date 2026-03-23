# pylint: skip-file

# DAY 15 - factorial


def factorial(number):
    frct = 1
    while number > 1:
        frct *= number
        number -= 1
    print(frct)


factorial(5)
