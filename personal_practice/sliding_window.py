def slide(arr: list, k):
    i = 0
    max = 0
    while i < len(arr) - k:
        new_max = sum([arr[i], arr[i + 1], arr[i + 2], arr[i + 3]])
        if new_max > max:
            max = new_max
        i += 1
    return max


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
print(slide(arr, 4))
