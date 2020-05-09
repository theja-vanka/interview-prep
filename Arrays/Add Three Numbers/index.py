def threeNumberSum(array, targetSum):
    array.sort()
    resarr = []
    for index in range(len(array)-2):
        i, j, k = index, index+1, len(array)-1
        while j < k:
            currentSum = array[i] + array[j] + array[k]
            if currentSum == targetSum:
                resarr.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif currentSum > targetSum:
                k -= 1
            else:
                j += 1
    return resarr
