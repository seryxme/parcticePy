def perm(str, str2: str):
    lst = list(str2)
    lst.reverse()
    str3 = "".join(lst)
    if str == str3:
        return True
    return False


print(perm("peek", "keep"))
print(perm("peek", "kept"))
# print(list("peek"))
