def prefix_average2(S):
    n = len(S)
    A = [0] * n
    for j in range(n):
        A[j] = sum(S[0:j + 1]) / (j + 1)  # record the average
    return A


def unique2(arr):
    temp = sorted(arr)
    for j in range(1, len(temp)):
        if arr[j - 1] == arr[j]:
            return False
    return True
