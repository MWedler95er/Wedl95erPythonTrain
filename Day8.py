
'''
Docstring for Day8

Set's  and Dictionary's 


!!! Set items are unordered, unchangeable and do not allow duplicate values !!!

Need to ask!!!!
    set order Boolean's (True, False, 0, 1) at the start of the unordered set 

'''


# Set
test_set_1 = { 1 , 2 , 3 , 4 , 5 , 6 }
test_set_2 = {"apple", "Apple","bannana","kiwi","melon"}
test_set_3 = {"water", 1 , "apple", True, 400, False, "melon"}
print(test_set_1,"\n",test_set_2,"\n",test_set_3)


# it isn't possible to insert duplecate values -> delete the all duplecates automaticlly, hold only the first
test_set_4 = {"water", 2, 2, "bannana", "bannana", 0, False , True, 1}
# 1 epual True | 0 epual False
print(test_set_4)

# Add and Remove Items 
# only one argument in ()!!
test_set_4.add("Apple")  
print(test_set_4)

#!!! Case-sensetiv !! 
test_set_4.remove(True) # throw a exeption when (###) is not in the set
print(test_set_4)

# test_set_4.clear() delete all items

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

# set Operations

# dont safe the .union(item's) in the origin set
# union the set by any Iterable
y = test_set_4.union(test_set_1) 
print(y)
print(test_set_4)
s = test_set_1 | test_set_2 | test_set_3
print(s)

# safe the changes in the origin set
# Update the set by any Iterable
update_set={"Berlin", "kiwi", 30, "berlin","bannana"}
test_set_4.update(update_set)
#test_set_4 |= update_set  #same aa .update()
print(test_set_4)

# intersection() return a set that contains similarity values, that exist in both+ sets
print("intersetion")
intersection = test_set_4.intersection(test_set_3)
print(intersection)
print(test_set_4)
# intersection = test_set_4 & test_set_3 # same as .intersection()

# intersection_update delete all items that not exist in both+ sets and update the fist set!
inter_update = test_set_4.intersection_update(test_set_3)
print(inter_update)
print(test_set_4)
# inter_update = test_set_4 &= test_set_3 # same as intersection_update()

# difference return a set of items, the set contain that exist only in the fist set an not in both+
print("difference")
diff = test_set_4.difference(test_set_3)
print(diff)
print(test_set_4)
# deff = test_set_4 - test_set_3 # same as .diffference()

# differance_update delete the items in the first set that are also in the other set's
#print("diff_update")
#print(test_set_4)
#diff_update = test_set_4.difference_update(test_set_3)
#print(diff_update) # is empty -> deleted
#print(test_set_4)
# deff_update = test_set_4 -= test_set_3 # same as .difference_update

# loop iterate 
# Same as List, Tuple

for set_item in test_set_4:
    print(set_item)



'''
        Dictionary
'''
# dictionary is a key:value list, can contains all data-typs
test_dict = {
    "name" : "michel",
    "age" : 30,
    "sex" : "m",
    "driver-licens" : False,
    "smoker" : False
}

# get a list of all key's 
print(test_dict.keys())

#get a list of all Values
print(test_dict.values())

# get one Value of a key
print(test_dict.get("name"))
print(test_dict.get("driver-licens"))

# Add a key:value paar
test_dict["hight"]=1.69
print(test_dict.get("hight"))

# edit a value
test_dict["smoker"]=True
print(test_dict.get("smoker"))

print(test_dict.get("hight"))
test_dict.update({"hight":2.50})
print(test_dict.get("hight"))


# Delete some key:values 
test_dict.pop("sex")
print(test_dict)

# Delete the last key:value
print(test_dict)
test_dict.popitem()
print(test_dict)

# Delete the hole key:values dictionary
#del test_dict
#print(test_dict)

# Delete the one key:values 
del test_dict["age"]
print(test_dict)

# loop thruegh a dictionary
for key in test_dict:
    print(key)
print()

for value in test_dict:
    print(test_dict[value])
print()

for key in test_dict.keys():
    print(key)
print()

for value in test_dict.values():
    print(value)
print()

for key,value in test_dict.items():
    print(key ,":", value)

# copy a Dictionary
test_dict_copy = test_dict.copy()
print(test_dict)
print(test_dict_copy)

del test_dict_copy #delete all key:values ind test_dict_copy
test_dict_copy = dict(test_dict)
print(test_dict_copy)

# nested dictonaries

fam_dict = {
    "schwester1" : {
       "name" : "Sia",
       "age": 31 
    },
    "schwester2":{
        "name" : "Pici",
        "age": 29 
    },
    "schwester3":{
        "name" : "Melina",
        "age": 17 
    },
    "bruder":{
        "name":"Valentin",
        "age":15
    }
}

print(fam_dict)    
# also ok
schwester1_2 = {
    "name" : "Sia",
    "age": 31 
}
schwester2_2={
    "name" : "Pici",
    "age": 29 
}
schwester3_2={
    "name" : "Melina",
    "age": 17 
}
bruder_2 ={
    "name":"Valentin",
    "age":15
}
fam_dict_2 = {
    "schwester1_2":schwester1_2,
    "schwester2_2":schwester2_2,
    "schwester3_2":schwester3_2,
    "bruder_2":bruder_2
}
print(fam_dict_2)

# print singel key value of one on sibling
print(fam_dict["schwester1"]["age"])
print(fam_dict_2["bruder_2"]["name"])

# loop through nested dictonaries
for sibling, key_value_dict in fam_dict.items(): #Vertikal
    print(sibling) 
    for key_value in key_value_dict: #Horizontal
        print(key_value,";",key_value_dict[key_value])


