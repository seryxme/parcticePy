def mySqrt(x: int) -> int:
    for num in range(1, x//2):
        if num * num == x:
            return num
        elif (num) * (num) > x:
            return num - 1


def my_sqrt(x: int) -> int:
    n = 1
    count = 0
    while x - n >= 0:
        x -= n
        count += 1
        n += 2
    return count


print(my_sqrt(224))