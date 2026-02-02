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
    return "even" if number % 2 == 0 else "odd"

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

''' DAY 15 '''

def factorial(number):
    frct = 1
    while number > 1:
        frct *= number
        number-=1
    print(frct)

factorial(5)

""" DAY 16 """

def palindrom(string):
    back_String = ""
    x = len(string)-1
    while x >= 0:
        back_String = back_String + string[x]
        x-=1
    
    if back_String == string:
        return True
    else:
        return False
    
print(palindrom("BooB"))

#pytonic way
def palindrom_2(string):
    return string.lower() == string[::-1].lower()

print(palindrom_2("Bob"))
print(palindrom_2("Boby"))


''' DAY 17 '''

# count the nuber of vowels in a String

def vowels_counter(text):
    counter = 0
    vowels = "a","e","i","o","u"
    for letters in text:
        if letters.lower() in vowels:
            counter+=1
    return counter

# Pythonic Way
def vowels_count(text):
    vowels = "aeiou"
    return sum( char in vowels for char in text.lower() )


print(vowels_counter("It's very cold outside"))
print(vowels_count("It's very cold outside"))



