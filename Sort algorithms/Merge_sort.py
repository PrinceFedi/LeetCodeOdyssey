def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        # Recursion to divide each array into sub-arrays (Divide step)
        merge_sort(left_array)
        merge_sort(right_array)

        i = 0  # the index of the leftest most items in my left array
        j = 0  # the index of the leftest most items in my right array
        k = 0  # the index of our new and combined array in our `Combination step`

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

# O(nlogn) time complexity
# O (n) space complexity
array1 = [5, 632, 6534, 7, 354, 53625.2534, 645]
print(array1)
merge_sort(array1)
print(array1)