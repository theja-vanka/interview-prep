def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey))
    return "".join(newLetters)


def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    if newLetterCode <= ord('z'):
        return chr(newLetterCode)
    else:
        return chr(ord('a') - 1 + newLetterCode % ord('z'))


def caesarCipherEncryptorAlternative(string, key):
    minChar = ord('a')
    maxChar = ord('z') + 1
    newString = ''
    key = key % (maxChar - minChar)
    for letter in string:
        newChar = (ord(letter) + key) % maxChar
        if newChar < minChar:
            newChar = newChar + minChar
        newString += chr(newChar)
    return newString
