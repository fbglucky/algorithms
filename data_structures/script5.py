def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""

    for k in range(1, len(A)):
        # Insert A[k] at its proper location within A[0], A[1], ..., A[k]. Noted: A[0, k - 1] is sorted
        curr = A[k]
        j = k  # find correct index j for current
        while j > 0 and A[j] > curr:  # element A[j-1] must be after current
            A[j] = A[j - 1]
            j -= 1
        A[j] = curr

