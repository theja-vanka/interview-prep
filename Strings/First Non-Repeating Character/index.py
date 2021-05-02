# O(N) time | O(1) space
def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:
            return idx
    return -1


# O(N) time | O(N) space
def firstNonRepeatingCharacterAlt(string):
    _ = []
    for index, character in enumerate(string):
        if character in string[index+1:] or character in _:
            _.append(character)
        else:
            return index
    return -1
