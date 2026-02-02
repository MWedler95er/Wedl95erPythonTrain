""" DAY 18 """
#Write a function to find the sum of all elements in a list.
def list_sum(list_objekt):
    return sum(list_objekt)

testlist=[1,3,5,8,13]
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

# oneliner
'''from functools import reduce
fib = lambda m: (a:=0, b:=1, [a := (tmp:=a, a:=b, b:=tmp+b)[0] for _ in range(m) if a <= m])[-1]


(a:=0, b:=1, ...): Wir initialisieren a und b direkt im Tuple.

tmp:=a, a:=b, b:=tmp+b: Das ist der Walrus-Trick, um das Tuple-Unpacking in einer List Comprehension zu simulieren.

if a <= m: Hier wird das Ende bei 174 (oder deinem Wert m) erzwungen.

[-1]: Am Ende nehmen wir das letzte Element des äußeren Tuples (unsere generierte Liste).

print(fib(174))
'''


''' DAY 21 '''
# reverse a list

def reverse_a_list(list_objk):
    rev_list = list(list_objk)
    rev_counter = 4
    for x in list_objk:
        print(x)
        rev_list[rev_counter] = x
        rev_counter-=1
    return rev_list

def reverse_a_list_wrong(list_objk):
    rev_list = list_objk # bildet eine reverence auf die liste keine Kopie
    rev_counter = len(list_objk)-1
    for x in list_objk:
        rev_list[rev_counter] = x
    return rev_list

print(reverse_a_list(testlist))

#pytonic way

def reverse_the_list(list_objk):
    return list_objk[::-1]

print(reverse_the_list(testlist))