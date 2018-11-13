def longest(prev, arr):
    if len(arr) == 0:
        return 0

    if arr[0] <= prev:
        return longest(prev, arr[1:])

    without_first = longest(prev, arr[1:])
    with_first = longest(arr[0], arr[1:]) + 1

    return max(with_first, without_first)


def lis(arr):
    return longest(-1, arr)


def construct_longest(prev, arr):
    if len(arr) == 0:
        return []

    if arr[0] <= prev:
        return construct_longest(prev, arr[1:])

    without_first = construct_longest(prev, arr[1:])

    with_first = [arr[0]] + construct_longest(arr[0], arr[1:])

    if len(without_first) > len(with_first):
        return without_first
    else:
        return with_first


def construct_lis(arr):
    return construct_longest(-1, arr)


