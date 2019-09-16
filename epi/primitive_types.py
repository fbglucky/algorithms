import csv
from pathlib import Path


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
    #main()
    print("Directory Path:", Path().absolute())

    Path().absolute()
    with open('ESL.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
