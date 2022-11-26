def find_unique(lst: list):
    lst2 = []
    for x in lst:
        if x not in lst2:
            lst2.append(x)
    return lst2


x = [1, 1, 3, 3, 4, 4, 4, 5]
print(find_unique(x))