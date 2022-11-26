def middle(lst: list):
    lst.pop(0)
    lst.pop()
    return lst


x=[1, 2, 3, 4, 5, 6, 7]
print(middle(x))