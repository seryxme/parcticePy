def unique_list(lst:list):
    for x in range(len(lst) - 1):
        if lst[x] in lst[(x+1):]:
            return False

    return True


arr1 = [2, 9, 6, 3, 12, 2, 4]
arr2 = [2, 3, 6, 9, 13, 21, 42]

print(unique_list(arr1))
print(unique_list(arr2))


def unique_list2(lst:list):
    lst2 = set(lst)
    if len(lst) == len(lst2):
        return True
    return False


print(unique_list2(arr1))
print(unique_list2(arr2))