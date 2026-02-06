"""
Create simple Arithmetic/-, Relational-Operators

"""


#  Arithmetic -Operators
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def floor_division(a, b):
    return a // b


def modulus(a, b):
    return a % b


def exponential(a, b):
    return a**b

    # Relational -Operators


def equal(a, b):
    return a == b


def not_equal(a, b):
    return a != b


def greater_than(a, b):
    return a > b


def lesser_than(a, b):
    return a < b


def greater_equal_than(a, b):
    return a >= b


def lesser_equal_than(a, b):
    return a <= b


print(" Addition 2 and 5")
print(addition(2, 5), "\n")
print("Subbtraction 2 from 5")
print(subtraction(2, 5), "\n")
print("mutiplicate 2 with 5")
print(multiplication(2, 5), "\n")
print("division 10 by 2")
print(division(10, 3), "\n")
print("floor division 10 by 3")
print(floor_division(10, 3), "\n")
print("modulu 10 by 3")
print(modulus(10, 3), "\n")
print("expotenzial 2 by 2")
print(exponential(2, 2), "\n")

print("is 2 and 2 equal")
print(equal(2, 2))
print("is 2 and 20 equal")
print(not_equal(2, 20), "\n")

print("is 2 and 2 equal")
print(not_equal(2, 2))
print("is 2 and 20 equal")
print(not_equal(2, 20), "\n")

print("is 2 grather than 10")
print(greater_than(2, 10))
print("is 10 grather than 2")
print(greater_than(10, 2), "\n")

print("is 2 lesser than 10")
print(lesser_than(2, 10))
print("is 10 lesser than 2")
print(lesser_than(10, 2), "\n")

print("is 2 grather or equal than 10")
print(greater_equal_than(2, 10))
print("is 2 grather or equal than 10")
print(greater_equal_than(2, 10))
print("is 10 grather or equal than 10")
print(greater_equal_than(10, 2), "\n")

print("is 2 grather or equal than 10")
print(lesser_equal_than(2, 10))
print("is 2 grather or equal than 10")
print(lesser_equal_than(2, 10))
print("is 10 grather or equal than 10")
print(lesser_equal_than(10, 10), "\n")
