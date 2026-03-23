#
#  List
#
# Create a List
TEST_LIST = ["apfel", 4, "2026-01-29", "blue", 500]

# Access Elements
print(TEST_LIST[0])
print(TEST_LIST[1])
print(TEST_LIST[2])
print(TEST_LIST[3])
print(TEST_LIST[4])

print(TEST_LIST[-1])
print(TEST_LIST[-2])
print(TEST_LIST[-3])
print(TEST_LIST[-4])
print(TEST_LIST[-5])

# slice the List
print(TEST_LIST[1:3])
print(TEST_LIST[:3])
print(TEST_LIST[3:])

# Modify the lList
print(TEST_LIST)
TEST_LIST.append("Baum")
TEST_LIST.append("Tree")

print(TEST_LIST)
TEST_LIST.insert(1, "apple")

print(TEST_LIST)
del TEST_LIST[-2]
del TEST_LIST[0]
print(TEST_LIST)
# del TEST_LIST[0:4]
# print(TEST_LIST)

# Iterate Through the List with "for" and "while"
for thing in TEST_LIST:
    print(thing)
print()

count = 0
while count < len(TEST_LIST):
    print(TEST_LIST[count])
    count += 1
print()

# ^^ with operations
for thing in TEST_LIST:
    if thing == 4:
        print("four")
    elif thing == 500:
        print("Chees")
    elif thing == "2026-01-29":
        print("a Good Day")
    else:
        print(thing)
print()


count = 0
while count < len(TEST_LIST):
    count += 1
    if count % 2 == 0:
        print("even count")
    else:
        print(TEST_LIST[count - 1])
print()

#
#  Tuples
#
# Create Tuple
test_tuples = ("tuple", True, 240, "branching", 3 + 4)
print(test_tuples)

# access, modify and slice the Tuple
print(test_tuples[1])
print(test_tuples[4])
print(test_tuples[-2])
print(test_tuples[3:-1])
print(test_tuples[:-1])

# Add in too Tuple
test_tuples += ("Git", "Python")
print(test_tuples)
# Multiply outcome
print(test_tuples * 3)
print(test_tuples[2] * 3)  # when Tuple[Index] is a Number then they do Math
print(
    test_tuples[0] * 3
)  # concatenation when Tuple[Index] is a String -> Without space between
# give index back
print(test_tuples.index("tuple"))
print(test_tuples.index(7))
# count summ
test_tuples += ("2", "2", "2", "2", "2")
print(test_tuples.count("2"))
# in opertion -> outcome True/False
print("Tuple" in test_tuples)  # outcome False
print("tuple" in test_tuples)  # outcome True
print(7 in test_tuples)  # outcome True
print(3 + 4 in test_tuples)  # outcome True
print(480 / 2 in test_tuples)  # outcome True


# convert to a List // First Try without Google the "right Way"

# first thought
#    - for loop -
#        each literation safe the tuple in a pre-createt list by using a pre-createt Index(i)
#    - same wiht while

converted_tuple_list = []
i = 0
for each_tuple_thing in test_tuples:
    converted_tuple_list.append(test_tuples[i])
    i += 1
print(converted_tuple_list)

converted_tuple_list.clear()  # delete all from the list
i = 0
while i < len(test_tuples):
    converted_tuple_list.append(test_tuples[i])
    i += 1
print(converted_tuple_list)


converted_tuple_list.clear()  # delete all from the list
# Googel for the "Right way" how i convert a Tuple in a List

converted_tuple_list = list(test_tuples)  # Viel sauberer! # wow simple
print(converted_tuple_list)


# testing some stuff
converted_tuple_list = ["Two" if x == "2" else x for x in test_tuples]  # wow simple
print(converted_tuple_list)

converted_tuple_list.clear()  # delete all from the list
for x in test_tuples:
    if x == "2":
        converted_tuple_list.append("Dos")
    else:
        converted_tuple_list.append(x)
print(converted_tuple_list)
