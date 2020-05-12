def productSum(array):
    return levelSum(array, 1)


def levelSum(array, multiplier):
    totalSum = 0
    for element in array:
        if type(element) == list:
            totalSum += levelSum(element, multiplier + 1)
        else:
            totalSum += element
    return totalSum * multiplier
