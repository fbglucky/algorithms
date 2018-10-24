import math


def count(target, data):
    n = 0
    for item in data:
        if item == target:
            n += 1
    return n


def factors(n):
    for k in range(1, n + 1):
        if n % k == 0:
            yield k


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_multiple(n, m):
    return True if n % m == 0 else False


def is_even(k):
    return k & 1


def min_max(data):
    if len(data) == 0:
        raise ValueError("There is no item in the list")

    min1, max1 = data[0], data[0]
    for item in data:
        max1 = max1 if max1 > item else item
        min1 = min1 if min1 < item else item
    return min1, max1


def sum_of_square(n):
    """Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n."""
    return sum(k * k for k in range(1, n))


def sum_of_odd_square(n):
    """Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n."""
    return sum(k * k for k in range(1, n) if k % 2 == 1)


def my_reversed(ls):
    return list(ls[i] for i in range(len(ls) - 1, -1, -1))


def product_is_odd(ls):
    odd_count = 0
    for item in ls:
        if odd_count == 2:
            return True
        if item % 2 == 1:
            odd_count = odd_count + 1


def is_different(ls):
    return len(set(ls)) == len(ls)


def out_of_bound():
    ls = [1, 2, 3]
    try:
        ls[4] = 5
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")


def count_vowels(str):
    vowels = {'a', 'i', 'u', 'e', 'o'}

    return sum(1 for k in str if k in vowels)


def remove_punctuation(str):
    punctuation = {',', '.', ':', ';', '!', '?', '\''}
    return ''.join(k for k in str if k not in punctuation)


def factors(n):
    k = 1
    while k * k < n:
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:
        yield k


def p_norm(v, p):
    return (sum(k ** p for k in v)) ** (1 / p)


def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]


def count_divide_times(n):

    if n <= 1:
        return 0
    return 1 + count_divide_times(n // 2)
