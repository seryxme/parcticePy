def ninty_deg(lst: list):
    lst.reverse()
    lst2 = [[] for i in range(len(lst))]
    for x in lst:
        for i in range(len(x)):
            lst2[i].append(x[i])

    return lst2


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(ninty_deg(arr))
