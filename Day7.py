testlist = ["apfel", 4, "2026-01-29", "blue", 500]

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

print(testlist[1:3])
print(testlist[:3])
print(testlist[3:])

print(testlist)
testlist.append("Baum")
testlist.append("Tree")

print(testlist)
testlist.insert(1,"apple")

print(testlist)
del testlist[-2]
del testlist[0]
print(testlist)
del testlist[0:4]
print(testlist)



