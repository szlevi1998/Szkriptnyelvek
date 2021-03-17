#!/usr/bin/env python3

""""
Ahhoz, hogy az évszámot megtaláljam a chrral megkerestem a megfelelőt amely ez: ߥ .
Ezután simán vettem ennek a chr-nak az összegét.
"""


def main():
    print(sum(ord(c) for c in "ߥ"))


if __name__ == "__main__":
    main()
