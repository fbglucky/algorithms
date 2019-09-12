def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1  # right shift 1 bit (/2), then reassign to itself (x)

    return num_bits


def main():
    print(16 << 1)  # 16 shifted left once = 16 * 2
    print(16 << 3)  # 16 shifted left triple = 16 * (2 * 3)
    print(128 >> 3)
    print(5 ^ 5)  # 0
    print(5 ^ 0)

    print(count_bits(20003))


if __name__ == "__main__":
    main()
