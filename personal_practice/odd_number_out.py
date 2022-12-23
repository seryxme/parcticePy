def odd_number_out(arr: list) -> int:
    even_num = []
    odd_num = []
    for x in arr:
        if x % 2 == 0:
            even_num.append(x)
        else:
            odd_num.append(x)

    if len(even_num) == 1:
        return even_num[0]
    return odd_num[0]


# x = [2, 4, 6, 2, 7, 20, 10]
# y = [3, 5, 9, 19, 18, 23, 27, 97, 63]
# print(odd_number_out(y))
