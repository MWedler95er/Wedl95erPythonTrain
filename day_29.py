from collections import Counter
"""

    DAY 29

#Create a dictinary of words an thir frequencies.

"""



def dict_word_frequency(dict_of_words):
    temp_list = []
    for value in dict_of_words.values():
        temp_list.extend(value.lower().split())
    return Counter(temp_list)


test_dict = {
    "key1": "hallo dass ist ein test ?",
    "key2": "alo ist das ein Test ?",
    "key3": "wen das ein test ist !",
    "key4": "wann ist der Test ? ",
}

print(dict_word_frequency(test_dict))

# Pythonic Way
# from collections import Counter


def dict_word_frequency2(dict_of_words):
    return Counter(
        word for value in dict_of_words.values() for word in value.lower().split()
    )
