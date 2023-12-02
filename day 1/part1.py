#!/usr/bin/env python3

"""The newly-improved calibration document consists of lines of text; each
line originally contained a specific calibration value that the Elves now
need to recover. On each line, the calibration value can be found by
combining the first digit and the last digit (in that order) to form a
single two-digit number.

For example:
1abc2       -> 12
pqr3stu8vwx -> 38
a1b2c3d4e5f -> 15
treb7uchet  -> 77

The sum of these calibration values is 142"""

INPUT_FILENAME = "input.txt"


def get_first_digit(string: str) -> str:
    """Returns the first digit in a string as a string."""
    for char in string:
        try:
            int(char)
            return char
        except ValueError:
            continue

    return ""


def get_last_digit(string: str) -> str:
    """Returns the last digit in a string as a string."""
    for i in range(len(string) - 1, -1, -1):
        char: str = string[i]

        try:
            int(char)
            return char
        except ValueError:
            continue

    return ""


def main():
    sum: int = 0

    with open(INPUT_FILENAME) as file:
        for line in file:
            number: int = int(get_first_digit(line) + get_last_digit(line))
            sum += number

    print(sum)


if __name__ == "__main__":
    main()
