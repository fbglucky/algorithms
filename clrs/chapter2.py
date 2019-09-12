def insert_sort(arr, comparator):
    for i in range(1, len(arr)):
        value = arr[i]
        # insert arr[i] into the sorted array a[0..i-1]
        j = i - 1
        while j >= 0 and comparator(value, arr[j]):
            # shift right one position
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value


ls = [31, 41, 59, 26, 41, 58]
insert_sort(ls, lambda x, y: x < y)


def add_n_bit_integer(i1, i2):
    result = [0] * (len(i1) + 1)

    for i in range(len(i1) - 1, -1, -1):
        # fill sum of i1[i] and i2[i] into result[i + 1] and keep carry_out in result[i]
        tmp = result[i] + i1[i] + i2[i]
        if tmp == 0 or tmp == 1:
            result[i + 1] = tmp
        elif tmp == 2:
            result[i + 1], result[i] = 0, 1
        else:
            result[i + 1], result[i] = 1, 1

    return ''.join(map(str, result))


def merge(arr1, arr2):
    result = [None] * (len(arr1) + len(arr2))
    i, j = 0, 0
    for k in range(0, len(result)):
        if j > len(arr2) - 1:
            result[k], i = arr1[i], i + 1
        elif i > len(arr1) - 1:
            result[k], j = arr2[j], j + 1
        elif arr1[i] < arr2[j]:
            result[k], i = arr1[i], i + 1
        else:
            result[k], j = arr2[j], j + 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr) // 2
        left = merge_sort(arr[0: middle])
        right = merge_sort(arr[middle: len(arr)])

        return merge(left, right)
