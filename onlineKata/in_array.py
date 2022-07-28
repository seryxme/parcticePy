def in_array(array1, array2):
    result = list({word for word in array1 for word_2 in array2 if word in word_2})
    result.sort()
    return result


print(in_array(["live", "arp", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))