def good_fibonacci(n):
    """ Return pair of Fibonacci numbers, F(n) and F(n-1)."""
    if n <= 1:
        return n, 0
    else:
        (a, b) = good_fibonacci(n - 1)

    return a + b, a


def reverse(S, start, stop):
    """Reverse elements in implicit slice S[start:stop]."""
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


def max_recuirsive(arr):
    """Describe a recursive algorithm for finding the maximum element in a sequence, S, of n elements. What is your running time and space usage?"""
    if len(arr) == 1:
        return arr[0]
    max(arr[0], max_recuirsive(arr[1:]))


def harmonic_number(n):
    """Describe a recursive function for computing the nth Harmonic number, H[n] = sum(1/i), for i = 1 to n."""
    if n == 1:
        return 1
    return 1/n + harmonic_number(n - 1)


def min_max(arr):
    """Write a short recursive Python function that finds the minimum and maximum values in a sequence without using any loops."""
    if len(arr) == 1:
        return arr[0], arr[0]

    min = arr[0]
    max = arr[0]

    new_min, new_max = min_max(arr[1:])
    if min > new_min:
        min = new_min
    if max < new_max:
        max = new_max
    return min, max
