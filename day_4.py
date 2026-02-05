class day_4:
    """
    Create simple Arithmetic/-, Relational-Operators

    """

    #  Arithmetic -Operators
    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b

    def multiplication(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b

    def floor_division(self, a, b):
        return a // b

    def modulus(self, a, b):
        return a % b

    def exponential(self, a, b):
        return a**b

        # Relational -Operators

    def equal(self, a, b):
        return a == b 

    def not_equal(self, a, b):
        return a != b   

    def greater_than(self, a, b):
        return a > b

    def lesser_than(self, a, b):
        return a < b

    def greater_equal_than(self, a, b):
        return a >= b

    def lesser_equal_than(self, a, b):
        return a <= b


show = day_4()

print(" Addition 2 and 5")
print(show.addition(2, 5), "\n")
print("Subbtraction 2 from 5")
print(show.subtraction(2, 5), "\n")
print("mutiplicate 2 with 5")
print(show.multiplication(2, 5), "\n")
print("division 10 by 2")
print(show.division(10, 3), "\n")
print("floor division 10 by 3")
print(show.floor_division(10, 3), "\n")
print("modulu 10 by 3")
print(show.modulus(10, 3), "\n")
print("expotenzial 2 by 2")
print(show.exponential(2, 2), "\n")

print("is 2 and 2 equal")
print(show.equal(2, 2))
print("is 2 and 20 equal")
print(show.equal(2, 20), "\n")

print("is 2 and 2 equal")
print(show.not_equal(2, 2))
print("is 2 and 20 equal")
print(show.not_equal(2, 20), "\n")

print("is 2 grather than 10")
print(show.greater_than(2, 10))
print("is 10 grather than 2")
print(show.greater_than(10, 2), "\n")

print("is 2 lesser than 10")
print(show.lesser_than(2, 10))
print("is 10 lesser than 2")
print(show.lesser_than(10, 2), "\n")

print("is 2 grather or equal than 10")
print(show.greater_equal_than(2, 10))
print("is 2 grather or equal than 10")
print(show.greater_equal_than(2, 10))
print("is 10 grather or equal than 10")
print(show.greater_equal_than(10, 2), "\n")

print("is 2 grather or equal than 10")
print(show.lesser_equal_than(2, 10))
print("is 2 grather or equal than 10")
print(show.lesser_equal_than(2, 10))
print("is 10 grather or equal than 10")
print(show.lesser_equal_than(10, 10), "\n")
