'''
Divide the array in different sets where number of sets is equal
 to GCD of n and d and move the elements within sets.
If GCD is 1 as is for the above example array (n = 7 and d =2),
 then elements will be moved within one set only,
 we just start with temp = arr[0] and keep moving arr[I+d] to arr[I] and
 finally store temp at the right place.

Here is an example for n =12 and d = 3. GCD is 3 and
Let arr[] be {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

a) Elements are first moved in first set
    arr[] after this step --> {4 2 3 7 5 6 10 8 9 1 11 12}
b) Then in second set.
    arr[] after this step --> {4 5 3 7 8 6 10 11 9 1 2 12}
c) Finally in third set.
    arr[] after this step --> {4 5 6 7 8 9 10 11 12 1 2 3}

'''


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def leftRotate(arr, d, n):
    d = d % n
    g_c_d = gcd(d, n)
    for i in range(g_c_d):
        # move i-th values of blocks
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if k >= n:
                k = k - n
            if k == i:
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
leftRotate(lst, 2, len(lst))
print(lst)
