# def divisible_by_3(number):
#     sum = 0
#     for x in range(len(str(number))):
#         sum += int(str(number)[x])
#     if sum % 3 == 0:
#         return True
#     return False
#
#
# print(divisible_by_3(11282881))
from math import sqrt


def sim(num):
    for factor in range(2, int(sqrt(num))):
        if num % factor == 0:
            return False

    return True

print(sim(11282881))
print(sqrt(11282881))