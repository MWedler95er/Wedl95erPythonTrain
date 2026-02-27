""" Bubbel sort und merge sort"""

class OwnSorter:

    def bubble_sort(list_with_numbers:list) -> list:
        list_len = len(list_with_numbers)
        for i in range(list_len-1):
            for j in range(list_len-i-1):
                if list_with_numbers[j] > list_with_numbers[j+1]:
                    list_with_numbers[j],list_with_numbers[j+1] = list_with_numbers[j+1],list_with_numbers[j]

        