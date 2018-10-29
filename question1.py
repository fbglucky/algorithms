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
