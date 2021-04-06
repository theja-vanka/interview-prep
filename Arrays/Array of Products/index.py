# O(n^2) time | O(n) space
def arrayOfProductsBrute(array):
    product = [1 for _ in array]
    for index, value in enumerate(array):
        for idx, val in enumerate(array):
            if idx != index:
                product[index] *= array[idx]
    return product


# O(n) time | O(n) space
def arrayOfProducts(array):
    product = [1 for _ in array]

    leftRunningProduct = 1
    for i in range(len(array)):
        product[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        product[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    return product
