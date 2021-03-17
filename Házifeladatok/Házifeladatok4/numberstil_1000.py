#!/usr/bin/env python3

def main():
    """"
    A listában összegyűjtjük a számokat 3-nak vagy 5-nek többszöröseit 0-1000-ig.
    Ebben a változóban a summal eltároljuk az összegyűjtött számoknak összegét.
    """
    list_of_numbers = sum([n for n in range(1, 999 + 1) if n % 3 == 0 or n % 5 == 0])

    """
    Printtel kiíratjuk a változónak az értéket.     
    """
    print("3-nak vagy 5-nek többszörösei összege: ", list_of_numbers)


if __name__ == "__main__":
    main()
