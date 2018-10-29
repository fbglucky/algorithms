from collections import defaultdict


def count_pairs1(arr, sum):
    result = set()

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == sum:
                result.add((arr[i], arr[j]))

    return result


# print(count_pairs1([4, 1, 7, 2, 3, 3, 7, 5, 6], 10))


def count_pairs2(arr, total):
    map_count = defaultdict(int)

    # Store counts of all elements in map m
    for i in range(len(arr)):
        map_count[arr[i]] += 1

    count = 0

    # loop through each element and increment the count (Notice that every pair is counted twice)
    for i in range(len(arr)):

        if total - arr[i] in map_count:
            count += 1
        # better, count full array, not distinct pairs
        # count += map_count[total - arr[i]]

        # do not count (arr[i], arr[i]) pair
        if total - arr[i] == arr[i]:
            count -= 1

    return int(count / 2)


print(count_pairs2([4, 1, 7, 2, 3, 3, 7, 5, 6], 10))
