# pylint: skip-file

# DAY 16 - palindrome


def palindrom(string):
    back_string = ""
    string_len = len(string) - 1
    while string_len >= 0:
        back_string = back_string + string[string_len]
        string_len -= 1

    if back_string == string:
        return bool(True)


print(palindrom("BooB"))


# pytonic way
def palindrom_2(string):
    return string.lower() == string[::-1].lower()


print(palindrom_2("Bob"))
print(palindrom_2("Boby"))
