def moveElementToEnd(array, toMove):
    for element in array:
        if toMove == element:
            array.remove(toMove)
            array.append(toMove)
    return array
