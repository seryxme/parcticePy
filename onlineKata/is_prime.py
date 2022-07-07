def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True

    for factor in range(2, number):
        if number % factor == 0:
            return False

    return True


print(is_prime(23))