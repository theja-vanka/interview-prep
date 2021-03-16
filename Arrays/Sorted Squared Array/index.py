def sortedSquaredArray(array):
    array = [x**2 for x in array]
    array.sort()
    return array


def sortedSquaredArray2(array):
    start = 0
    end = len(array) - 1
    returnarr = []
    while start <= end:
        smallvalue = array[start]
        largevalue = array[end]
        if abs(smallvalue) > abs(largevalue):
            returnarr.insert(0, smallvalue**2)
            start += 1
        else:
            returnarr.insert(0, largevalue**2)
            end -= 1
    return returnarr


def sortedSquaredArray3(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares
