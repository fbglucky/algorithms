def merge(ar1, ar2):

    if len(ar1) == 0:
        return ar2
    if len(ar2) == 0:
        return ar1

    if ar1[0] < ar2[0]:
        ar1, ar2 = ar2, ar1

    return [ar1[0]] + merge(ar1[1:], ar2)


merge([1, 5, 9, 10, 15, 20], [2, 3, 8, 13])
