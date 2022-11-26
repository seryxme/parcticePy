def highest_score(lst: list):
    highest = lst[0]
    second_highest = lst[0]
    for score in lst:
        if score > highest:
            second_highest = highest
            highest = score

    return highest, second_highest


x = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45]

print(highest_score(x))
