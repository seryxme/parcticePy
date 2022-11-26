def roman_to_int(s: str) -> int:
    conv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    integer_sum = 0
    for i in range(len(s)):
        if i > 0:
            if conv[s[i]] > conv[s[i - 1]]:
                integer_sum += (conv[s[i]] - (2 * conv[s[i - 1]]))
                continue
        integer_sum += conv[s[i]]

    return integer_sum


roman = "CMXLIV"
print(roman_to_int(roman))
# print(y)
