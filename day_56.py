"""Bubbel sort und merge sort"""


class OwnSorter:
    def bubble_sort(
        self, list_with_numbers: list
    ) -> list:  #!!!sortiert die list und überschreibt sie!!!
        list_len = len(list_with_numbers)
        for i in range(list_len - 1):
            for j in range(list_len - i - 1):
                if list_with_numbers[j] > list_with_numbers[j + 1]:
                    list_with_numbers[j], list_with_numbers[j + 1] = (
                        list_with_numbers[j + 1],
                        list_with_numbers[j],
                    )


sorter = OwnSorter()

test_list = [100, 50, 56, 23, 36, 67, 3, 734, 4]

sorter.bubble_sort(test_list)
print(test_list)
