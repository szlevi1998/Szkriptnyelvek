#!/usr/bin/env/ python3


def main():
    print("Adj meg egy számot!")
    szam = input()
    forditott = str(szam)[::-1]

    if forditott[0] == "0":
        print("A szám utolsó számjegye 0 ezért ezt nem lehet megfordítani")
    else:
        print("A megfordított szám : ", forditott)


if __name__ == '__main__':
    main()
    input()
