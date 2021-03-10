#!/usr/bin/env python3

def main():
    szamok = list(range(1, 101))

    atvaltas = ''.join([str(elem) for elem in szamok])

    szamjegyek_osszege = sum(int(digit) for digit in atvaltas)
    print(szamjegyek_osszege)


if __name__ == "__main__":
    main()
