'''
3768 = 1701 * 2 + 366
1701 = 366 * 4 + 237
366 = 237 * 1 + 129
237 = 129 * 1 + 108
129 = 108 * 1 + 21
108 = 21 * 1 + 3
21 = 3 * 7 + 0

Hence 3 is the gcd
'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(1701, 3768))  # Answer should be 3
