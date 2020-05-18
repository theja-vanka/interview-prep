def isMonotonic(array):
    if len(array) <= 2:
        return True
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue
        if breakDirection(direction, array[i - 1], array[i]):
            return False
    return True


def breakDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0


def isMonotonicAlternative(array):
    if len(array) <= 2:
        return True
    else:
        j = 1
        aflag = array[0] <= array[2]
        dflag = array[0] > array[2]
        while j < len(array):
            if array[j - 1] <= array[j] and aflag:
                j += 1
            elif array[j - 1] >= array[j] and dflag:
                j += 1
            else:
                return False
    return True

