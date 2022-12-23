from typing import List


def longest_common_prefix(strs: List[str]) -> str:
    prefix = ""
    next_prefix = ""
    for char in strs[0]:
        next_prefix += char
        for word in strs:
            if not word.startswith(next_prefix):
                return prefix
        prefix = next_prefix
    return prefix


def longestCommonPrefix(strs: List[str]) -> str:
    if len(strs) == 0:
        return ""

    if len(strs) == 1:
        return strs[0]

    word_dict = dict()
    word = strs[0]
    prefix = ""
    for char in word:
        prefix += char
        word_dict[prefix] = 0
    if len(word_dict) == 0:
        return ""

    count = 0
    for key in word_dict:
        for word in strs:
            if word.startswith(key):
                count += 1
            if not word.startswith(key):
                count = 0
                break
        word_dict[key] = count
        count = 0

    prefix = list(word_dict.keys())[0]
    for key in word_dict:
        if word_dict[key] >= word_dict[prefix]:
            prefix = key
        elif word_dict[key] == word_dict[prefix] and len(key) > len(prefix):
            prefix = key

    if word_dict[prefix] <= 1:
        return ""
    return prefix


strs = ["flower", "flow", "flight", "flowing"]

print(longest_common_prefix(strs))

strs = ["dog", "racecar", "car", "racer", "racing"]

print(longest_common_prefix(strs))

strs = ["aba","c","b","a","ab"]

print(longest_common_prefix(strs))


