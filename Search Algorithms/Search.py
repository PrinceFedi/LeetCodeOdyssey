# ------------------------------------------- Linear Search --------------------------------------------------


def Linear_Search(array, value):
    for i in range(len(array)):
        if value == array[i]:
            return i
    else:
        return False

# ------------------------------------------- Binary Search --------------------------------------------------

def Binary_Search(sorted_array, value):
    left_pointer = 0
    right_pointer = len(sorted_array) - 1
    middle = 0
    while left_pointer <= right_pointer:
        middle = (right_pointer +left_pointer ) // 2

        # If value is greater, ignore left half
        if value > sorted_array[middle]:
            left_pointer = middle + 1

        elif value < sorted_array[middle]:
            right_pointer = middle- 1

        else:
            return f"element is present at index {middle}"

    return False


array = sorted([1,2,3,4,5,6,7,8, 435,6543])
print(Binary_Search(array, 435))