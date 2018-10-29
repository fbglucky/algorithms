from nltk.corpus import words


def splittable(arr):
    if len(arr) == 0:
        return True

    for i in range(len(arr)):
        if is_word(arr[:i + 1]):
            if splittable(arr[i + 1:]):
                return True

    return False


def is_word(arr):
    return ''.join(arr) in words.words()
