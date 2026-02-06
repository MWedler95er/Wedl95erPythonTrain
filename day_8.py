"""
Docstring for Day8

Set's  and Dictionary's


!!! Set items are unordered, unchangeable and do not allow duplicate values !!!

Need to ask!!!!
    set order Boolean's (True, False, 0, 1) at the start of the unordered set

"""

# Set
TEST_SET_1 = {1, 2, 3, 4, 5, 6}
TEST_SET_2 = {"apple", "Apple", "bannana", "kiwi", "melon"}
TEST_SET_3 = {"water", "apple", True, 400, False, "melon"}
print(TEST_SET_1, "\n", TEST_SET_2, "\n", TEST_SET_3)


# it isn't possible to insert duplecate values ->
#   delete the all duplecates automaticlly, hold only the first
TEST_SET_4 = {"water", 2, "bannana", 0, 1}
# 1 epual True | 0 epual False
print(TEST_SET_4)

# Add and Remove Items
# only one argument in ()!!
TEST_SET_4.add("Apple")
print(TEST_SET_4)

#!!! Case-sensetiv !!
TEST_SET_4.remove(True)  # throw a exeption when (###) is not in the set
print(TEST_SET_4)

# TEST_SET_4.clear() delete all items

#!!! Case-sensetiv !!
TEST_SET_4.discard("apple")  # throw no exeptions by missing (####)
TEST_SET_4.discard("A pple")  # throw no exeptions by missing (####)
print(TEST_SET_4)

# .pop() remove one Random item fom the set -> allways the same through programm starts
# sets are Unorderd -> but .pop() delete allwasy the index[0]
x = TEST_SET_4.pop()
print(x)
print(TEST_SET_4)
x = TEST_SET_4.pop()
print(x)
print(TEST_SET_4)

# set Operations

# dont safe the .union(item's) in the origin set
# union the set by any Iterable
y = TEST_SET_4.union(TEST_SET_1)
print(y)
print(TEST_SET_4)
s = TEST_SET_1 | TEST_SET_2 | TEST_SET_3
print(s)

# safe the changes in the origin set
# Update the set by any Iterable
update_set = {"Berlin", "kiwi", 30, "berlin", "bannana"}
TEST_SET_4.update(update_set)
# TEST_SET_4 |= update_set  #same aa .update()
print(TEST_SET_4)

# intersection() return a set that contains similarity values, that exist in both+ sets
print("intersetion")
intersection = TEST_SET_4.intersection(TEST_SET_3)
print(intersection)
print(TEST_SET_4)
# intersection = TEST_SET_4 & TEST_SET_3 # same as .intersection()

# intersection_update delete all items that not exist in both+ sets and update the fist set!
TEST_SET_4.intersection_update(TEST_SET_3)
print(TEST_SET_4)
# inter_update = TEST_SET_4 &= TEST_SET_3 # same as intersection_update()

# difference return a set of items, the set contain that exist only in the fist set an not in both+
print("difference")
diff = TEST_SET_4.difference(TEST_SET_3)
print(diff)
print(TEST_SET_4)
# deff = TEST_SET_4 - TEST_SET_3 # same as .diffference()

# differance_update delete the items in the first set that are also in the other set's
# print("diff_update")
# print(TEST_SET_4)
# diff_update = TEST_SET_4.difference_update(TEST_SET_3)
# print(diff_update) # is empty -> deleted
# print(TEST_SET_4)
# deff_update = TEST_SET_4 -= TEST_SET_3 # same as .difference_update

# loop iterate
# Same as List, Tuple

for set_item in TEST_SET_4:
    print(set_item)


# DICTIONARY
# dictionary is a key:value list, can contains all data-typs
TEST_DICT = {
    "name": "michel",
    "age": 30,
    "sex": "m",
    "driver-licens": False,
    "smoker": False,
}

# get a list of all key's
print(TEST_DICT.keys())

# get a list of all Values
print(TEST_DICT.values())

# get one Value of a key
print(TEST_DICT.get("name"))
print(TEST_DICT.get("driver-licens"))

# Add a key:value paar
TEST_DICT["hight"] = 1.69
print(TEST_DICT.get("hight"))

# edit a value
TEST_DICT["smoker"] = True
print(TEST_DICT.get("smoker"))

print(TEST_DICT.get("hight"))
TEST_DICT.update({"hight": 2.50})
print(TEST_DICT.get("hight"))


# Delete some key:values
TEST_DICT.pop("sex")
print(TEST_DICT)

# Delete the last key:value
print(TEST_DICT)
TEST_DICT.popitem()
print(TEST_DICT)

# Delete the hole key:values dictionary
# del TEST_DICT
# print(TEST_DICT)

# Delete the one key:values
del TEST_DICT["age"]
print(TEST_DICT)

# loop thruegh a dictionary
for key in TEST_DICT:
    print(key)
print()

for value in TEST_DICT.items():
    print(TEST_DICT[value])
print()

for key in TEST_DICT:
    print(key)
print()

for value in TEST_DICT.values():
    print(value)
print()

for key, value in TEST_DICT.items():
    print(key, ":", value)

# copy a Dictionary
TEST_DICT_COPY = TEST_DICT.copy()
print(TEST_DICT)
print(TEST_DICT_COPY)

del TEST_DICT_COPY  # delete all key:values ind test_dict_copy
TEST_DICT_COPY = dict(TEST_DICT)
print(TEST_DICT_COPY)

# nested dictonaries

FAM_DICT = {
    "schwester1": {"name": "Sia", "age": 31},
    "schwester2": {"name": "Pici", "age": 29},
    "schwester3": {"name": "Melina", "age": 17},
    "bruder": {"name": "Valentin", "age": 15},
}

print(FAM_DICT)
# also ok
schwester1_2 = {"name": "Sia", "age": 31}
schwester2_2 = {"name": "Pici", "age": 29}
schwester3_2 = {"name": "Melina", "age": 17}
bruder_2 = {"name": "Valentin", "age": 15}
FAM_DICT_2 = {
    "schwester1_2": schwester1_2,
    "schwester2_2": schwester2_2,
    "schwester3_2": schwester3_2,
    "bruder_2": bruder_2,
}
print(FAM_DICT_2)

# print singel key value of one on sibling
print(FAM_DICT["schwester1"]["age"])
print(FAM_DICT_2["bruder_2"]["name"])

# loop through nested dictonaries
for sibling, key_value_dict in FAM_DICT.items():  # Vertikal
    print(sibling)
    for key, value in key_value_dict.items():  # Horizontal (geändert)
        print(key, ";", value)
