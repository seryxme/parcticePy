import math
import string

char62array = string.ascii_letters + "0123456789"
remainder_list = []


def convert_key(key):
    if key < 62:
        return char62array[key]

    divisor = key
    while divisor != 0:
        remainder_list.insert(0, divisor % 62)
        divisor = divisor // 62

    converted_key = ""
    for remainder in remainder_list:
        converted_key += char62array[int(remainder)]

    remainder_list.clear()
    return converted_key


def retrieve_key(converted_key):
    key = 0;
    for letter in converted_key:
        for char in char62array:
            if letter == char:
                key += char62array.index(char) * math.pow(62, len(converted_key) - (converted_key.index(letter) + 1))
                break

    return int(key)
