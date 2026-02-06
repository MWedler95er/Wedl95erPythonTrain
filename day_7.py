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

COUNT = 0
while COUNT < len(TEST_LIST):
    print(TEST_LIST[COUNT])
    COUNT += 1
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


COUNT = 0
while COUNT < len(TEST_LIST):
    COUNT += 1
    if COUNT % 2 == 0:
        print("even count")
    else:
        print(TEST_LIST[COUNT - 1])
print()

#
#  Tuples
#
# Create Tuple
TEST_TUPLES = ("tuple", True, 240, "branching", 3 + 4)
print(TEST_TUPLES)

# access, modify and slice the Tuple
print(TEST_TUPLES[1])
print(TEST_TUPLES[4])
print(TEST_TUPLES[-2])
print(TEST_TUPLES[3:-1])
print(TEST_TUPLES[:-1])

# Add in too Tuple
TEST_TUPLES += ("Git", "Python")
print(TEST_TUPLES)
# Multiply outcome
print(TEST_TUPLES * 3)
print(TEST_TUPLES[2] * 3)  # when Tuple[Index] is a Number then they do Math
print(
    TEST_TUPLES[0] * 3
)  # concatenation when Tuple[Index] is a String -> Without space between
# give index back
print(TEST_TUPLES.index("tuple"))
print(TEST_TUPLES.index(7))
# count summ
TEST_TUPLES += ("2", "2", "2", "2", "2")
print(TEST_TUPLES.count("2"))
# in opertion -> outcome True/False
print("Tuple" in TEST_TUPLES)  # outcome False
print("tuple" in TEST_TUPLES)  # outcome True
print(7 in TEST_TUPLES)  # outcome True
print(3 + 4 in TEST_TUPLES)  # outcome True
print(480 / 2 in TEST_TUPLES)  # outcome True


# convert to a List // First Try without Google the "right Way"

# first thought
#    - for loop -
#        each literation safe the tuple in a pre-createt list by using a pre-createt Index(i)
#    - same wiht while

converted_tuple_list = []
i = 0
for each_tuple_thing in TEST_TUPLES:
    converted_tuple_list.append(TEST_TUPLES[i])
    i += 1
print(converted_tuple_list)

converted_tuple_list.clear()  # delete all from the list
i = 0
while i < len(TEST_TUPLES):
    converted_tuple_list.append(TEST_TUPLES[i])
    i += 1
print(converted_tuple_list)


converted_tuple_list.clear()  # delete all from the list
# Googel for the "Right way" how i convert a Tuple in a List

converted_tuple_list = list(TEST_TUPLES)  # Viel sauberer! # wow simple
print(converted_tuple_list)


# testing some stuff
converted_tuple_list = ["Two" if x == "2" else x for x in TEST_TUPLES]  # wow simple
print(converted_tuple_list)

converted_tuple_list.clear()  # delete all from the list
for x in TEST_TUPLES:
    if x == "2":
        converted_tuple_list.append("Dos")
    else:
        converted_tuple_list.append(x)
print(converted_tuple_list)
