def is_prime(num: int) -> bool:
    from math import sqrt
    def divisible_by_3(number):
        sum = 0
        for x in range(len(str(number))):
            sum += int(str(number)[x])
        if sum % 3 == 0:
            return True
        return False

    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num < 10000:
        for factor in range(2, num):
            if num % factor == 0:
                return False
    elif (num % 10) % 2 == 0 or (num % 10) % 5 == 0:
        return False
    elif divisible_by_3(num):
        return False
    else:
        for factor in range(2, int(sqrt(num)) + 1):
            if is_prime(factor):
                if num % factor == 0:
                    return False

    return True


print(is_prime(11282881))