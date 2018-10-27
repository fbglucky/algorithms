import functools


def edit_distance(s1, s2):
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)

    # the last entry in the bottom row is empty
    last_bottom_empty = edit_distance(s1[:-1], s2) + 1
    # the last entry in the top row is empty
    last_top_empty = edit_distance(s1, s2[:-1]) + 1

    # both rows have chars in the last column, so check if these chars are different or not
    last_exist = edit_distance(s1[:-1], s2[:-1]) + 1 if s1[-1] != s2[-1] else 0

    return min(last_bottom_empty, last_top_empty, last_exist)
