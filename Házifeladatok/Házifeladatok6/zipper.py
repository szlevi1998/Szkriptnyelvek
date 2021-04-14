#!/usr/bin/env python3


def main():
    karakter = "abcdefghijklmnopqrstuvwxyz"
    ascii_number = list(range(ord('a'), ord('z')+1))

    for i in zip(karakter, ascii_number):
        print(i)


if __name__ == "__main__":
    main()

