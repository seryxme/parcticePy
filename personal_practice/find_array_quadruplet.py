def find_array_quadruplet(arr, s):
    i = 0
    max = 0
    while i < len(arr) - 4:
        new_arr = [arr[i], arr[i + 1], arr[i + 2], arr[i + 3]]
        new_sum = sum(new_arr)
        if new_sum == s:
            return new_arr
        i += 1
    return []

    # for i in range(len(arr) - 4):
    #     j = i + 3
    #     new_array = [arr[0], arr[1], arr[2], arr[j]]
    #     quad_sum = sum(new_array)
    #     if quad_sum == sum:
    #         return sorted(new_array)
    #
    # for i in range(len(arr) - 5):
    #     j = i + 3
    #     new_array = [arr[0], arr[1], arr[j], arr[j + 1]]
    #     quad_sum = sum(new_array)
    #     if quad_sum == sum:
    #         return sorted(new_array)
    #
    # for i in range(len(arr) - 6):
    #     j = i + 3
    #     new_array = [arr[0], arr[j], arr[j + 1], arr[j + 2]]
    #     quad_sum = sum(new_array)
    #     if quad_sum == sum:
    #         return sorted(new_array)
    #
    # for i in range(len(arr) - 4):
    #     new_array = [arr[i], arr[i + 1], arr[i + 2], arr[i + 3]]
    #     quad_sum = sum(new_array)
    #     if quad_sum == sum:
    #         return sorted(new_array)


lst = [2, 7, 4, 0, 9, 5, 1, 3]
print(find_array_quadruplet(lst, 10))
