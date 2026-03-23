# pylint: skip-file

# DAY 17 - count the number of vowels in a string


def vowels_counter(text):
    counter_vowels = 0
    vowels = "a", "e", "i", "o", "u"
    for letters in text:
        if letters.lower() in vowels:
            counter_vowels += 1
    return counter_vowels


# Pythonic Way
def vowels_count(text):
    vowels = "aeiou"
    return sum(char in vowels for char in text.lower())


print(vowels_counter("It's very cold outside"))
print(vowels_count("It's very cold outside"))
