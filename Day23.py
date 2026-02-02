""" DAY 23 """
# write a funciton to find the intersection of two lists.

list_objk1 = [ 1,2,3,4,5]
list_objk2 = [ 10,2,3,4,5]

def interselection_objk(list_objk1,list_objk2):
    objk1 = set(list_objk1)
    objk2 = set(list_objk2)
    return objk1.intersection(objk2) #!! unsauber gibt set zurück kein list

print(interselection_objk(list_objk1,list_objk2))

def interselection_objk2(list_objk1,list_objk2):
    objk1, objk2 = set(list_objk1), set(list_objk2)
    return list(objk1.intersection(objk2))

print(interselection_objk2(list_objk1,list_objk2))

#pytoic way

def interselection_objk_py_way(list_objk1,list_objk2):
    return list(set(list_objk1)& set(list_objk2))

print(interselection_objk_py_way(list_objk1,list_objk2))

''' DAY 24 '''
# write a funcion to convert a list of words into a sentence
list_w = ["Hallo", "ich", "mag", "python"]
def sentence_maker(list_w):
    sentence = ""
    for x in list_w:
        sentence += x+" "
    return sentence
print(sentence_maker(list_w))

#pytonic way
def sentence_maker(list_w):
    sentence = " ".join(list_w)   # join -> only for list with strings in it -> return a new String
    return f"{sentence.capitalize()}."  # .capitalize => fist letter Big!! 

""" DAY 25 """
sentece = "That is a test String, an it is a bad String"
def word_conter(sentence):
    splitet = sentence.split()
    count_frequence = {}
    for x in splitet:
        if count_frequence.keys() == x:
            count_frequence[x]=count_frequence.get(x) +1 
        else:
            count_frequence[x]=1
    return count_frequence
            

print(word_conter(sentece))