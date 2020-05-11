def isPalindromeRecursive(string):
    return checkAlpha(string[0], string[-1], string[1:-1])


def checkAlpha(alphabet1, alphabet2, pstring):
    if alphabet1 == alphabet2:
        if len(pstring) == 1 or len(pstring) == 0:
            return True
        return checkAlpha(pstring[0], pstring[-1],pstring[1:-1])
    else:
        return False


def isPalindromeAlternative(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString
