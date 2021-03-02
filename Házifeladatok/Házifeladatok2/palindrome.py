#!/usr/bin/env python3

def palindrome(s):
    if s == s[::-1]:
        return print("Palindróm a(z)", s, "szó")
    else:
        return print('Nem palindróm a(z)', s, "szó")


def main():
    print("Adj meg egy szöveget")
    text = input()
    palindrome(text)


if __name__ == '__main__':
    main()
