def insertion_sort(array):
    length = (len(array))
    for i in range(1, length):
        for j in range(i - 1, -1, -1):  # Loop through all the elements on the left side
            if array[j] > array[j + 1]:  # if the item on the right of the index is less then the item on the left then
                array[j], array[j + 1] = array[j + 1], array[j]  # they'll swap place
            else:
                break  # its found its position, and we can now go to the i loop


def sort_insertion(array):
    length = (len(array))
    for i in range(1, len(array)):
        j = i - 1
        while array[j] > array[j + 1] and j >= 0:
            array[j], array[j + 1] = array[j + 1], array[j]  # they'll swap place
            j -= 1


array = [7, 8, 5, 4, 9, 2]
insertion_sort(array)
print(array)
