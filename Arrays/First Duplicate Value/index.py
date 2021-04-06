# O(n) time | O(1) space
def firstDuplicateValue(array):
    for value in array:
        print(array)
        absValue = abs(value)
        if array[absValue - 1] < 0:
            print(absValue, array[absValue - 1])
            return absValue
        array[absValue - 1] *= -1
    return -1


def firstDuplicateValueAlt(array):
    for index, value in enumerate(array):
        negation = value * -1
        if negation in array:
            return negation * -1
        else:
            array[index] = negation
    return -1


# O(n) time | O(n) space
def firstDuplicateValueN(array):
    seen = set()
    for value in array:
        if value in seen:
            return value
        seen.add(value)
    return -1


# O(n^2) time | O(1) space
def firstDuplicateValueBrute(array):
    minimumvalue = len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                minimumvalue = min(minimumvalue, j)

    if minimumvalue == len(array):
        return -1

    return array[minimumvalue]
