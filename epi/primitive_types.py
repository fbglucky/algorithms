def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1

    return num_bits


def main():
    print(count_bits(20003))


if __name__ == "__main__":
    main()
