import sys

from url_shortener import shorten_url, retrieve_url


def shorten_long_url():
    long_url = input("Enter the website link to convert: ")
    print(shorten_url(long_url))
    main_menu()


def retrieve_long_url():
    short_url = input("Enter the short link to retrieve your website link: ")
    print(retrieve_url(short_url))
    main_menu()


def main_menu():
    option = int(input("""
                    Welcome to Seryx Link Shortener App.
                    What would you like to do?
                    1. Shorten a link
                    2. Retrieve a link
                    0. Exit
                    """))

    match option:
        case 1:
            shorten_long_url()
        case 2:
            retrieve_long_url()
        case 0:
            sys.exit(0)


main_menu()
