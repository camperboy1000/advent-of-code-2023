#!/usr/bin/env python3

"""Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and
last digit on each line. For example:

two1nine         -> 29
eightwothree     -> 83
abcone2threexyz  -> 13
xtwone3four      -> 24
4nineeightseven2 -> 42
zoneight234      -> 14
7pqrstsixteen    -> 76

The sum of these calibration values is 281"""


INPUT_FILENAME = "input.txt"

VALID_DIGITS: dict[str, int] = dict()
VALID_DIGITS["one"] = 1
VALID_DIGITS["two"] = 2
VALID_DIGITS["three"] = 3
VALID_DIGITS["four"] = 4
VALID_DIGITS["five"] = 5
VALID_DIGITS["six"] = 6
VALID_DIGITS["seven"] = 7
VALID_DIGITS["eight"] = 8
VALID_DIGITS["nine"] = 9


def get_first_digit(string: str) -> str:
    """Returns the first digit in a string as a string.
    Parses both actual numbers and spelled out numbers."""

    int_digit: str = ""
    str_digit: str = ""
    int_index: int = -1
    str_index: int = -1

    for i in range(len(string)):
        char: str = string[i]

        try:
            int(char)
            int_index = i
            int_digit = char
            break
        except ValueError:
            continue

    for number in VALID_DIGITS.keys():
        index: int = string.find(number)

        if index == -1:
            continue
        elif str_index == -1 or index < str_index:
            str_index = index
            str_digit = str(VALID_DIGITS[number])

    if (int_index < str_index or str_index == -1) and int_index != -1:
        return int_digit
    elif str_index < int_index or int_index == -1:
        return str_digit
    else:
        return ""


def get_last_digit(string: str) -> str:
    """Returns the last digit in a string as a string.
    Parses both actual numbers and spelled out numbers."""

    int_digit: str = ""
    str_digit: str = ""
    int_index: int = -1
    str_index: int = -1

    for i in range(len(string) - 1, -1, -1):
        char: str = string[i]

        try:
            int(char)
            int_index = i
            int_digit = char
            break
        except ValueError:
            continue

    for number in VALID_DIGITS.keys():
        index: int = string.rfind(number)

        if index == -1:
            continue
        elif str_index == -1 or index > str_index:
            str_index = index
            str_digit = str(VALID_DIGITS[number])

    if (int_index > str_index or str_index == -1) and int_index != -1:
        return int_digit
    elif str_index > int_index or int_index == -1:
        return str_digit
    else:
        return ""


def main():
    sum: int = 0

    with open(INPUT_FILENAME) as file:
        for line in file:
            number: int = int(get_first_digit(line) + get_last_digit(line))
            print(number)
            sum += number

    print(sum)


if __name__ == "__main__":
    main()
