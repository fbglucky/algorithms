def has_array_two_candidates(arr, total):
    """
    Write a program that, given an array A[] of n numbers and another number x,
    determines whether or not there exist two elements in S whose sum is exactly x.
    """
    # Create an empty hash set
    s = set()

    result = []
    for i in range(len(arr)):
        temp = total - arr[i]
        if temp >= 0 and temp in s:
            result.append((arr[i], temp))
        s.add(arr[i])

    return result


# driver program to check the above function
A = [1, 4, 45, 6, 10, 7]
n = 11
print(has_array_two_candidates(A, n))


def find_pairs(arr1, arr2, total):
    arr1_set = set(arr1)

    result = set()

    for item in arr2:
        if total - item in arr1_set:
            result.add((item, total - item))

    return result


# arr1 = [1, 0, -4, 7, 6, 4]
# arr2 = [0, 2, 4, -3, 2, 1]
# x = 8
# print(find_pairs(arr1, arr2, x))


# Given an integer array and a positive integer k, count all distinct pairs with difference equal to k.
def count_dif_k(arr, k):
    count = 0

    arr_set = set(arr)

    for item in arr:
        if item - k in arr_set or item + k in arr_set:
            count += 1
        arr_set.remove(item)

    return count


# print(count_dif_k([1, 5, 3, 4, 2], 3))
