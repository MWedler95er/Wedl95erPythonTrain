"""DAY 54 - List Comprehensions"""

test_list = ["hallo", "oh'zapft ist", "oberklasse", "nether", "obstobatzer"]


def o_zeahler(words_list):
    return sum(1 for word in words_list for char in word if char.lower() == "o")


print(o_zeahler(test_list))

zahlen_list = [1, 3, 5, 7, 8, 10, 11, 13, 14]


def avg_odd_zahlenliste(zahlen_liste):
    return sum(1 for zahlen in zahlen_liste if zahlen % 2 == 1)


# für eine zahl in liste +1 sum wenn zahlen modulu 2 = 1(ungerade)

print(avg_odd_zahlenliste(zahlen_list))


def avg_even_zahlenliste(zahlen_liste):
    return sum(1 for zahlen in zahlen_liste if zahlen % 2 == 0)


# für eine zahl in liste +1 sum wenn zahlen modulu 2 = 1(gerade)

print(avg_even_zahlenliste(zahlen_list))
