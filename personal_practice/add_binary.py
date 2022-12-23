def bin_to_dec(bin_str):
    str_len = len(bin_str)
    dec_val = 0
    i = 0
    for x in range(str_len-1, -1, -1):
        dec_val += int(bin_str[i]) * (2**x)
        i += 1

    return dec_val


def dec_to_bin(dec_val):
    new_val = dec_val
    bin_arr = []
    while new_val != 0:
        rem = str(new_val % 2)
        bin_arr.append(rem)
        new_val //= 2
    bin_arr.reverse()
    return "".join(bin_arr)


def addBinary(a: str, b: str) -> str:
    return dec_to_bin((bin_to_dec(a) + bin_to_dec(b)))
    # return (bin(int(a, 2) + int(b, 2)))[2:]



a = "1011"
b = "11"
c = 12
print(addBinary(a, b))

expected = "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000"
print(expected == addBinary("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101",
                "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011"))