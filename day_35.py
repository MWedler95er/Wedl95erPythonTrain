"""

    DAY 35
# Calculate the average of numbers in a text file.

"""


def calc_summ_from_txt(file_name):
    numbers = []
    file_sum = int(0)
    with open(file_name, "r") as f:
        for line in f:
            numbers = line.split()
    for number in numbers:
        file_sum += int(str(number))
    return file_sum


file_n = "testText.txt"

print(calc_summ_from_txt(file_n))


# Pythonic Way
def calc_summ_from_txt_pw(file_name):
    with open(file_name, "r") as f:
        numbers = [int(num) for line in f for num in line.split() if num.strip()]
    return sum(numbers)


print(calc_summ_from_txt_pw(file_n))
