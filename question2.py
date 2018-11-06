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


def count_pairs3(arr1, arr2, value):
    count = 0
    left = 0
    right = len(arr2) - 1

    while left < len(arr1) and right >= 0:
        # if this sum is equal to value, then increment 'left', decrement 'right' and increment'count'
        if arr1[left] + arr2[right] == value:
            left = left + 1
            right = right - 1
            count = count + 1

        # if this sum is less than value, then increment left
        elif (arr1[left] + arr2[right]) < value:
            left = left + 1

        # else decrement 'right'
        else:
            right = right - 1

    return count


def find_triplet(arr, total):
    count = 0

    for i in range(len(arr)):
        # Find pair in sub array arr[i+1..n-1]
        # with sum equal to sum - arr[i]
        s = set()
        curr_sum = total - arr[i]
        for j in range(i + 1, len(arr)):
            if (curr_sum - arr[j]) in s:
                count += 1
            s.add(arr[j])

    return count


def count_missing(arr, low, high):

    arr_set = set(arr)
    result = []
    for item in range(low, high):
        if item not in arr_set:
            result.append(item)

    return result



