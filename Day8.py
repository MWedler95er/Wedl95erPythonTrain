'''
Docstring for Day8

Set's  and Dictionary's 


!!! Set items are unordered, unchangeable and do not allow duplicate values !!!
!!! set order Boolean's (True, False, 0, 1) at the start of the unordered set!!! 

'''


# Set

test_set_1 = { 1 , 2 , 3 , 4 , 5 , 6 }
test_set_2 = {"apple", "Apple","bannana","kiwi","melon"}
test_set_3 = {"water", 1 , "apple", True, 400, False, "melon"}
print(test_set_1,"\n",test_set_2,"\n",test_set_3)


# it isn't possible to insert duplecate values -> delete the all duplecates automaticlly, hold only the first(!!! case-insensetiv !!!)
test_set_4 = {"water", 2, 2, "bannana", "bannana", 0, False , True, 1}
# 1 epual True | 0 epual False
print(test_set_4)

''' Add and Remove Items '''
# only one argument in ()!!
test_set_4.add("Apple")  
print(test_set_4)

# Update the set by any Iterable - !!!! ignors duplicate rule !!!! 
update_set={"Berlin", "kiwi", 30, "berlin"}
test_set_4.update(update_set)
print(test_set_4)

#!!! Case-sensetiv !! 
test_set_4.remove(True) # throw a exeption when (###) is not in the set
print(test_set_4)

#!!! Case-sensetiv !! 
test_set_4.discard("apple") # throw no exeptions by missing (####)
test_set_4.discard("A pple") # throw no exeptions by missing (####)
print(test_set_4)

# .pop() remove one Random item fom the set -> allways the same through programm starts
# sets are Unorderd -> but .pop() delete allwasy the index[0] 
x = test_set_4.pop()
print(x)
print(test_set_4)
x = test_set_4.pop()
print(x)
print(test_set_4)