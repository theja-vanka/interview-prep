# Best -> O(n) time | O(1) space
# Avgerage -> O(n^2) time | O(1) space
# Worst -> O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def insertionSortAlternative(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                pass
    return array
