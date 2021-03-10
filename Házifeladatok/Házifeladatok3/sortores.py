#!/usr/bin/env python3

import random as r

UPTO = 100


def main():
    first = 0

    for i in range(UPTO):
        print(r.randint(0, 9), end="")
        first += 1
        if first == 10:
            print("\t")
            first -= 10


if __name__ == '__main__':
    main()
