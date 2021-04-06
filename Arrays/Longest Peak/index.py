# O(n) time | O(1) space
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array) - 1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not isPeak:
            i += 1
            continue

        leftidx = i - 2
        while leftidx >= 0 and array[leftidx] < array[leftidx + 1]:
            leftidx -= 1
        rightidx = i + 2
        while rightidx < len(array) and array[rightidx] < array[rightidx - 1]:
            rightidx += 1

        currentPeakLength = rightidx - leftidx - 1
        longestPeakLength = max(longestPeakLength, currentPeakLength)
        i = rightidx
    return longestPeakLength
