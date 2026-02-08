class Day5:
    def __init__(self):
        pass

    def odd_or_even(self, number):
        return "Even" if number % 2 == 0 else "Odd"

    def age_kategories(self, number):
        if number >= 45:
            print("Senior")
        elif number >= 18:
            print("Adult")
        elif number >= 14:
            print("Teenager")
        else:
            print("Child")

    def addition_largest_numbers(self, a, b, c):
        if a >= b >= c:
            print(a, " and ", b, " are the two largest numbers ")
        elif b >= a >= c:
            print(b, " and ", a, " are the two largest numbers ")
        else:
            print(a, " and ", c, " are the two largest numbers ")

    def loop_addition(self, a):
        for n in range(1, a + 1):
            na = a
            na += n
        print(na)

    def factorial_of_number(self, d):
        factorial = 1
        number = d
        while number > 1:
            factorial *= number
            number -= 1
        print(factorial)


out = Day5()

print(out.odd_or_even(int(input(" Odd number "))))
print(out.odd_or_even(int(input(" Odd number "))) + "\n")
out.age_kategories(int(input("kinder alter Angeben: ")))
out.age_kategories(int(input("teenager age ")))
out.age_kategories(int(input("adult age ")))
out.age_kategories(int(input("senior age ")))
print()
out.loop_addition(
    int(input("a posetiv number to calculate the sum up to the number: "))
)
out.factorial_of_number(int(input("please just positiv numbers: ")))
