#!/usr/bin/env python3


def main(szam):
    if szam >= 1:
        main(szam // 2)
    print(szam % 2, end='')


if __name__ == '__main__':
    main(35)
