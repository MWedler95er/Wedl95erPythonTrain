# pylint: skip-file

# DAY 12 - odd or even


def odd_or_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


odd_or_even(3)


def odd_or_even_sec(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


print(odd_or_even_sec(3))


# pythonic way
def odd_or_even_sec_1(number):
    return "even" if number % 2 == 0 else "odd"


# pythonic way 2
def odd_or_even_sec_2(number):
    return ("Even", "Odd")[number % 2]
