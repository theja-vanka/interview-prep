def twoNumberSum(array, targetSum):
    # Write your code here.
    arrdict = {}
    for i in array:
        if i in arrdict:
            return [i, arrdict[i]]
        else:
            arrdict[targetSum-i] = i
    return []
