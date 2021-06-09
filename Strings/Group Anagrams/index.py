def groupAnagrams(words):
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())


def groupAnagramsStock(words):
    if len(words) == 0:
        return []

    sortedWords = ["".join(sorted(w)) for w in words]
    indices = [i for i in range(len(words))]
    indices.sort(key=lambda x: sortedWords[x])
    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]
    for index in indices:
        word = words[index]
        sortedWord = sortedWords[index]

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)
            continue

        result.append(currentAnagramGroup)
        currentAnagramGroup = [word]
        currentAnagram = sortedWord
    result.append(currentAnagramGroup)

    return result


def groupAnagramsAlt(words):
    if len(words) == 0:
        return []
    strlst = []
    for index, string in enumerate(words):
        string = list(string)
        string.sort()
        strlst.append((string, index))
    strlst.sort()
    left = 0
    right = 1
    returnlst = []
    _ = [words[strlst[left][1]]]
    while right < len(words):
        print(strlst[left], strlst[right])
        if strlst[left][0] == strlst[right][0]:
            _.append(words[strlst[right][1]])
            right += 1
        else:
            returnlst.append(_)
            left = right
            _ = []
            _.append(words[strlst[left][1]])
            right += 1
    returnlst.append(_)
    return returnlst
