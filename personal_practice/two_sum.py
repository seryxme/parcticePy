def two_sum(list_of_nums: list, target: int) -> list:
    sum_indexes = []

    for x in range(len(list_of_nums)):
        for y in range(x+1, len(list_of_nums)):
            if list_of_nums[x] + list_of_nums[y] == target:
                sum_indexes.append(x)
                sum_indexes.append(y)

    return sum_indexes


print(two_sum([3, -1, -4, -8, 7], -1))