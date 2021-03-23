#!/usr/bin/env python3

def main():
    megadott_szam = 2 ** 1000
    ertek = 0
    for szamjegy in str(megadott_szam):
        ertek += int(szamjegy)

    print(ertek)


if __name__ == "__main__":
    main()
