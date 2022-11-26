def diagonal(lst: list):
    sum_of_diagonal = 0
    for i in range(len(lst)):
        sum_of_diagonal += lst[i][i]

    return sum_of_diagonal


x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [[1, 2], [3, 4]]
print(diagonal(x))
print(diagonal(y))
