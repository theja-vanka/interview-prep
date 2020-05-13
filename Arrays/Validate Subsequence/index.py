def isValidSubsequence(array, sequence):
    itrstart = 0
    for number in array:
        if itrstart < len(sequence) and sequence[itrstart] == number:
            itrstart += 1
    return itrstart == len(sequence)
