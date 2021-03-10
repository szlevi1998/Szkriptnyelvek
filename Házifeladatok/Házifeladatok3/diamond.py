#!/usr/bin/env python3

def diamond_printer(rows):
    i = 1
    while i < rows:
        szoveg = "*" * i
        print(szoveg.center(rows, " "), end="")
        print()
        i += 2

    while i > 0:
        szoveg = "*" * i
        print(szoveg.center(rows, " "), end="")
        print()
        i -= 2


def main():
    print("Adj meg egy számot!")
    a = int(input())

    if a % 2 == 0:
        print("A megadott paraméter:", a, "páros, ami nem érvényes!")
    else:
        diamond_printer(a)


#############################################################################
if __name__ == "__main__":
    main()
