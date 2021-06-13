def minimumCharactersForWordsAlt(words):
    hashmap = {}
    for word in words:
        _ = {}
        for letter in word:
            if letter in _:
                _[letter] += 1
            else:
                _[letter] = 1
        for character in _:
            if character in hashmap:
                if _[character] > hashmap[character]:
                    hashmap[character] = _[character]  
            else:
                hashmap[character] = _[character]
    lst = []
    for character in hashmap:
        _ = [character for i in range(hashmap[character])]
        lst += _
    return lst


def minimumCharactersForWords(words):
    maximumCharacterFrequencies = {}

    for word in words:
        characterFrequencies = countCharacterFrequencies(word)
        updateMaximumFrequencies(characterFrequencies, maximumCharacterFrequencies)

    return makeArrayFromCharacterFrequencies(maximumCharacterFrequencies)


def countCharacterFrequencies(string):
    characterFrequencies = {}

    for character in string:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0

        characterFrequencies[character] += 1

    return characterFrequencies


def updateMaximumFrequencies(frequencies, maximumFrequencies):
    for character in frequencies:
        frequency = frequencies[character]

        if character in maximumFrequencies:
            maximumFrequencies[character] = max(frequency, maximumFrequencies[character])
        else:
            maximumFrequencies[character] = frequency


def makeArrayFromCharacterFrequencies(characterFrequencies):
    characters = []

    for character in characterFrequencies:
        frequency = characterFrequencies[character]

        for _ in range(frequency):
            characters.append(character)
    return characters
