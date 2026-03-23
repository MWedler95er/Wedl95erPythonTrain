# pylint: skip-file

# DAY 13 - biggest number of three


def biggest_number_of_three(number1, number2, number3):
    largest_nr = 0
    if number1 > number2:
        largest_nr = number1
    else:
        largest_nr = number2
    if largest_nr < number3:
        largest_nr = number2
    print(largest_nr)


biggest_number_of_three(2, 15, 5)


# pythonic way
def largest_of_3(number1, number2, number3):
    largest_nr = max(number1, number2, number3)
    return largest_nr


print(largest_of_3(2, 15, 10))
