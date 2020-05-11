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
    minChars = ord('a')
    maxChars = 26 + ord('a')
    newString = ''
    key = key % 26
    for char in string:
        currChar = (ord(char) + key) % maxChars
        if currChar < minChars:
            currChar += minChars
        newString = newString + chr(currChar)
    return newString
