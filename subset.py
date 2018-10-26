def subset(arr, total):
    if total == 0:
        return True
    elif total < 0 or len(arr) == 0:
        return False

    last_elm = arr[-1]
    with_last = subset(arr[:-1], total - last_elm)
    without_last = subset(arr[:-1], total)

    return with_last or without_last


def construct_subset(arr, total):
    if total == 0:
        return []
    elif total < 0 or len(arr) == 0:
        return None

    last_elm = arr[-1]
    without_last = construct_subset(arr[:-1], total)
    if without_last is not None:
        return without_last

    with_last = construct_subset(arr[:-1], total - last_elm)
    if with_last is not None:
        return list(set().union(with_last, [last_elm]))

    return None
