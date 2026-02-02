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
sentece = "That is a test String and it is a bad String and so that is a bad String"

# keine rücksichtname auf Lower
def word_count(sentence):
    splitet = sentence.split()
    count_frequence = {}
    for word in splitet:
        count_frequence[word]=None
    for x in splitet:
        if count_frequence.get(x) == None:
            count_frequence[x]=1
        else:
            count_frequence[x]+=1
    return count_frequence
            
print(word_count(sentece))

# Pytonic Way 
from collections import Counter
import re

def count_word_frequence(sentence):
    words = re.findall(r'\w+',sentece.lower())
    return Counter(words)

print(count_word_frequence(sentece))


''' DAY 26 '''
#Write a function check if two strings are anagrams.
w1 = "sei dena"
w2 = "die nase"
def anagram(word1,word2):
    w1 = []
    w2 = []
    for x in word1:
        w1.append(x)
    for x in word2:
        w2.append(x)
    w1 = set(w1)
    w2 = set(w2)
    pruf = w1.intersection(w2)
    if len(pruf) == len(w1) == len(w2):
        return True
    else: 
        return False
    
print(anagram(w1,w2))

#pytonisc way

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

print(is_anagram(w1,w2))


""" DAY 27"""

sentence2 = "This is a Good sentence for a test!"
def largest_word(sentence):
    words = sentence.split()
    l_word = words[0]
    for x in words:
        if len(x) > len(l_word):
            l_word = x
    return l_word

print(largest_word(sentence2))

#Pythonic Way
def largest_word2(sentence):
    words = sentence.split()
    return max(words, key=len) if words else ""

print(largest_word2(sentence2))

''' DAY 28 '''
# revers word in a sentence

def rev_sentence(sentence):
    words = sentence.split()
    rev_words = []
    for x in words:
        rev_words.append(x[::-1])
    sen = " ".join(rev_words)
    return sen

print(rev_sentence(sentence2))

#Pythonic Way

def rev_sentence_2(sentence):
    return " ".join(word[::-1] for word in sentence.split())
print(rev_sentence_2(sentence2))
