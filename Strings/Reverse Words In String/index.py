def reverseWordsInString(string):
    lst = []
    returnstring = ""
    for index in string:
        if index != " ":
            returnstring += index
        else:
            lst.append(returnstring)
            returnstring = ""
    lst.append(returnstring)
    lst = " ".join(lst[::-1])
    return lst


def reverseWordsInStringAlt(string):
    words = []
    startOfWord = 0
    for idx in range(len(string)):
        character = string[idx]
        if character == " ":
            words.append(string[startOfWord:idx])
            startOfWord = idx
        elif string[startOfWord] == " ":
            words.append(" ")
            startOfWord = idx
    words.append(string[startOfWord:])
    reverseList(words)
    return "".join(words)


def reverseList(lst):
    start, end = 0, len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1


def reverseWordsInStringHard(string):
    characters = [char for char in string]
    reversedListRange(characters, 0, len(characters) - 1)
    startOfWord = 0
    while startOfWord < len(characters):
        endOfWord = startOfWord
        while endOfWord < len(characters) and characters[endOfWord] != " ":
            endOfWord += 1
        reversedListRange(characters, startOfWord, endOfWord - 1)
        startOfWord = endOfWord + 1
    return "".join(characters)


def reversedListRange(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
