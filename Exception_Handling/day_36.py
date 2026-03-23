"""

    DAY 36
#Handle exeptions for division by zero

"""


def div_exception(nbr1, nbr2):
    try:
        ans = nbr1 / nbr2
        return ans
    except ZeroDivisionError:
        return "ERROR: Division by 0!"


print(div_exception(5, 0))
