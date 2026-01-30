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

