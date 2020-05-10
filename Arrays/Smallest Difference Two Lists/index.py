def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    indexone = 0
    indextwo = 0
    current = float('inf')
    smallest = float('inf')
    while indexone < len(arrayOne) and indextwo < len(arrayTwo):
        firstNumber = arrayOne[indexone]
        secondNumber = arrayTwo[indextwo]
    if firstNumber < secondNumber:
        current = secondNumber - firstNumber
        indexone += 1
    elif firstNumber > secondNumber:
        current = firstNumber - secondNumber
        indextwo += 1
    else:
        return [firstNumber, secondNumber]
    if smallest > current:
        smallest = current
        smallestPair = [firstNumber, secondNumber]
    return smallestPair
