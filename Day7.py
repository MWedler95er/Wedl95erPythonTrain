
#
#  List
#
# Create a List
testlist = ["apfel", 4, "2026-01-29", "blue", 500]

#Access Elements
print(testlist[0])
print(testlist[1])
print(testlist[2])
print(testlist[3])
print(testlist[4])

print(testlist[-1])
print(testlist[-2])
print(testlist[-3])
print(testlist[-4])
print(testlist[-5])

#slice the List
print(testlist[1:3])
print(testlist[:3])
print(testlist[3:])

#Modify the lList
print(testlist)
testlist.append("Baum")
testlist.append("Tree")

print(testlist)
testlist.insert(1,"apple")

print(testlist)
del testlist[-2]
del testlist[0]
print(testlist)
#del testlist[0:4]
#print(testlist)

# Iterate Through the List with "for" and "while"
for thing in testlist:
    print(thing)
print()

count = 0
while count < len(testlist):
    print(testlist[count])
    count += 1
print()

# ^^ with operations
for thing in testlist:
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
while count < len(testlist):
    count += 1
    if count % 2 == 0:
        print("even count")
    else :
        print(testlist[count])
print( )

#
#  Tuples
#
# Create Tuple
testTuples = ("tuple", True, 240, "branching", 3+4)
print(testTuples)

# access, modify and slice the Tuple
print(testTuples[1])
print(testTuples[4])
print(testTuples[-2])
print(testTuples[3:-1])
print(testTuples[:-1])

#Add in too Tuple
testTuples +=("Git", "Python")
print(testTuples)
#Multiply outcome 
print(testTuples *3)
print(testTuples[2]*3) # when Tuple[Index] is a Number then they do Math
print(testTuples[0]*3) # concatenation when Tuple[Index] is a String -> Without space between 
#give index back
print(testTuples.index("tuple"))
print(testTuples.index(7))
# count summ
testTuples +=("2","2","2","2","2")
print(testTuples.count("2"))
# in opertion -> outcome True/False
print("Tuple" in testTuples) # outcome False
print("tuple" in testTuples) # outcome True
print(7 in testTuples) # outcome True 
print(3+4 in testTuples) # outcome True 
print(480/2 in testTuples) # outcome True 


# convert to a List // First Try without Google the "right Way"

''' first thought 
    - for loop - each literation safe the tuple in a pre-createt list by using a pre-createt Index(i)
    - same wiht while
'''
converted_tuple_list = []
i = 0 
for each_tuple_thing in testTuples:
    converted_tuple_list.append(testTuples[i])
    i += 1
print(converted_tuple_list) 

converted_tuple_list.clear() # delete all from the list
i=0
while i < len(testTuples):
    converted_tuple_list.append(testTuples[i]) 
    i+=1
print(converted_tuple_list)


converted_tuple_list.clear() # delete all from the list
''' Googel for the "Right way" how i convert a Tuple in a List''' 

converted_tuple_list = [ x for x in testTuples] # wow simple 
print(converted_tuple_list)


#testing some stuff 
converted_tuple_list = ["Two" if x == "2" else x for x in testTuples] # wow simple 
print(converted_tuple_list)

converted_tuple_list.clear() # delete all from the list
for x in testTuples:
    if x == "2":
        converted_tuple_list.append("Dos")
    else:
        converted_tuple_list.append(x)
print(converted_tuple_list)
