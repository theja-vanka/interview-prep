def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else "BLUE"
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFirstRow == "RED":
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True


def classPhotosAlt(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    if redShirtHeights[0] <= blueShirtHeights[0]:
        default = True
    else:
        default = False

    for red, blue in zip(redShirtHeights, blueShirtHeights):
        if blue <= red and default:
            return False
        if red <= blue and not default:
            return False
    return True
