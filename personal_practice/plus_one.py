from typing import List


def plusOne(digits: List[int]) -> List[int]:
    digits_str = [str(x) for x in digits]
    number = int("".join(digits_str))
    number += 1
    num_str = str(number)
    new_digits = [int(char) for char in num_str]

    return new_digits


def plus_one(digits: List[int]) -> List[int]:
    digits.reverse()
    new_digits = []

    for x in digits:
        if x + 1 > 9:
            new_digits.append(0)
        else:
            new_digits.append(x + 1)
            break

    if len(new_digits) < len(digits):
        for x in range(len(new_digits), len(digits)):
            new_digits.append(digits[x])

    if new_digits[len(new_digits) - 1] == 0:
        new_digits.append(1)

    new_digits.reverse()
    return new_digits



a = [1, 9, 9]
print(plus_one(a))

