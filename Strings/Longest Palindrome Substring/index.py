def longestPalindromicSubstring(string):
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindromeFrom(string, i - 1, i + 1)
        even = getLongestPalindromeFrom(string, i - 1, i)
        longest = max(odd, even, key=listmax)
        currentLongest = max(longest, currentLongest, key=listmax)
    return string[currentLongest[0]:currentLongest[1]]


def listmax(x):
    return x[1] - x[0]


def getLongestPalindromeFrom(string, leftidx, rightidx):
    while leftidx >= 0 and rightidx < len(string):
        if string[leftidx] != string[rightidx]:
            break
        leftidx -= 1
        rightidx += 1
    return [leftidx + 1, rightidx]


def longestPalindromicSubstringAlt(string):
    longest = ""
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if len(substring) > len(longest) and isPalindrome(substring):
                longest = substring
    return longest


def isPalindrome(string):
    leftidx = 0
    rightidx = len(string) - 1
    while leftidx < rightidx:
        if string[leftidx] != string[rightidx]:
            return False
        leftidx += 1
        rightidx -= 1
    return True
