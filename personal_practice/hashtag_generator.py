def generate_hashtag(s):
    result = "#" + "".join([words.capitalize() for words in s.split(" ")])
    return False if s == "" or len(result) > 140 else result


s = "I love JavaPy and React Script along with other types of languages"
print(generate_hashtag(s))