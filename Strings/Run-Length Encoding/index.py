def runLengthEncoding(string):
    newalpha = string[0]
    counter = 1
    returnstring = ""
    for index in range(1, len(string), 1):
        if newalpha != string[index]:
            returnstring += counterReturn(counter, newalpha)
            newalpha = string[index]
            counter = 1
        else:
            counter += 1
    returnstring += counterReturn(counter, newalpha)
    return returnstring


def counterReturn(counter, alphabet):
    string = ""
    while counter > 9:
        string += f"{9}{alphabet}"
        counter -= 9
    string += f"{counter}{alphabet}"
    return string
