def string_of_sum(lst: list, k: int):
    lst2 = []
    for x in lst:
        if k - x in lst:
            lst2.append(f"{x} + {k - x}")
            lst.remove(x)
            lst.remove(k - x)

    return lst2


x = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
print(string_of_sum(x, 7))
