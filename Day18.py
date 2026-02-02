""" DAY 18 """
#Write a function to find the sum of all elements in a list.
def list_sum(list_objekt):
    return sum(list_objekt)

testlist=[1,2,3,4,5]
print(list_sum(testlist))


''' DAY 19 '''
#Write a function to find the maximum element in a list.

def max_element(list_of_numbers):
    return max(list_of_numbers)

print(max_element(testlist))

def fibonacci_sequence(max_value):
    number = [ 1, 1, 0]
    loop_condition = 1
    while loop_condition <= max_value: 
        number[2] = number[0] + number[1]
        number[0],number[1] = number[1],number[2]
        if loop_condition + number[2] < max_value:
            loop_condition = number[2]
        else:
            return number[2]

print(fibonacci_sequence(174))

# Genetator ansatz
def fibonacci_generator(max_value):
    a,b = 0,1
    while a <= max_value:
        yield a
        a,b = b, a+b

for x in fibonacci_generator(235):
    print(x)