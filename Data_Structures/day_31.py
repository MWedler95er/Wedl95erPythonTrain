"""DAY 31 - Merge two dictionaries."""


def merge_dict(dict1, dict2):
    for key in dict2:
        dict1[key] = dict2.get(key)
    return dict1


# Pythonic way
def merge_dict_pw(dict1, dict2):
    return dict1 | dict2


DICT_1 = {"name": "Valentin", "age": 15, "sex": "m"}
DICT_2 = {"name": "Melina", "age": 17, "hobby": "malen"}
print(merge_dict(DICT_1, DICT_2))
print(merge_dict_pw(DICT_1, DICT_2))
