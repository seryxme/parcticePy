import key_converter

url_dict = {}


def add_url(key, long_url):
    url_dict[key] = long_url


def get_url(key):
    return url_dict[key]


def convert_key(key):
    return key_converter.convert_key(key)


def shorten_url(long_url):
    key = len(url_dict)
    add_url(key, long_url)
    return "https://www.my_url.com/" + convert_key(key)


def retrieve_url(short_url):
    link_array = short_url.split("/")
    key = key_converter.retrieve_key(link_array[len(link_array) - 1])
    return get_url(key)


