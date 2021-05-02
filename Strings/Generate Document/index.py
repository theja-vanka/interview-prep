
# O(N) time | O(N) space
def generateDocument(characters, document):
    hashmap = {}
    for letter in characters:
        if letter in hashmap:
            hashmap[letter] += 1
        else:
            hashmap[letter] = 1
    for letter in document:
        if letter in hashmap:
            hashmap[letter] -= 1
            if hashmap[letter] < 0:
                return False
        else:
            return False
    return True
