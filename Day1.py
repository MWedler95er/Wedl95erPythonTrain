print("Hello, World!")

# One-liner comment
'''
this is a multi-line comment
'''

""" DAY 9 """

# random number
import random

x = random.randint(1,100)
print(x)

""" DAY 10 """
# loop 
for x in range(10):
    print(x)

''' DAY 11 '''
#while loop that print only odd numbers from 1 to 20 
counter = 0
while counter < 20:
    if counter%2==0:
        print(counter)
    counter+=1

''' DAY 12 '''
def odd_or_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
odd_or_even(3)

# if method return some thin it need to Printet 
def odd_or_even_sec(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(odd_or_even_sec(3))

#pythonic way
def odd_or_even_sec(number):
    return "even" if numer % 2 == 0 else "odd"

#pythonic way 2
def odd_or_even_sec(number):
    return ("Even", "Odd")[number % 2]

""" DAY 13 """
def biggest_number_of_three(number1, number2, number3):
    largest_nr = 0
    if number1 > number2:
        largest_nr = number1
    else:
        largest_nr = number2
    if largest_nr < number3:
        largest_nr = number2
    print(largest_nr)
biggest_number_of_three(2,15,5)

#pythonic way
def largest_of_3(number1, number2, number3):
    largest_nr = max(number1, number2, number3)
    return largest_nr
print(largest_of_3(2,15,10))

