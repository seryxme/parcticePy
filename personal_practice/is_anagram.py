import collections


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t) or len(s) == 0:
        return False

    t_list = [letter for letter in t]
    for alpha in s:
        if alpha in t_list:
            t_list.remove(alpha)

    if len(t_list) == 0:
        return True
    return False


def is_anagram(s: str, t: str) -> bool:
    return collections.Counter(s) == collections.Counter(t)


# print(isAnagram("race", "are"))
print(is_anagram("rat", "tar"))