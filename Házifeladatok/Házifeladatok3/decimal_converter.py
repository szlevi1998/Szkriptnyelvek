#!/usr/bin/env python3

def decimaltobinary(szam):
    if szam >= 1:
        decimaltobinary(szam // 2)

    print(szam % 2, end='')


def main():
    print("Adj meg egy számot!")
    input_szam = input()
    decimaltobinary(int(input_szam))


if __name__ == '__main__':
    main()
