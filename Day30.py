'''
            DAY 30

        # Sort a list of fnumbers in ascending order.

        
            DAY 31

        # Merge two dictionaries
'''
#30
def ascending_order(list_nubr):
    return list_nubr[::-1]

list_nubr = [ 1, 2,3,4,5,6,7,8,9,10]

print(ascending_order(list_nubr))

#31
def merge_dict(dict1,dict2):
    for key in dict2:
            dict1[key]=dict2.get(key)
    return dict1

#Pyhtonic way
def merge_dict_pw(dict1,dict2):
     return dict1 | dict2


dict1 = {
    "name":"Valentin",
    "age":15,
    "sex" : "m"
}
dict2 = {
    "name" : "Melina",
    "age": 17,
    "hobby":"malen"
}
print(merge_dict(dict1,dict2))
print(merge_dict_pw(dict1,dict2))
