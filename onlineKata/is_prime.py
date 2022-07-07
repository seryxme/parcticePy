def is_prime(number:int) -> bool:
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True

    for factor in range(2, num):
        if num % factor == 0:
            return False

    return True


print(is_prime(23))