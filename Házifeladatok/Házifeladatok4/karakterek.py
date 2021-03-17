#!/usr/bin/env python3

"""
Üres string létrehozok a foundletters változóban.
Ezután az if-ben megnézzzük, hogy vannak olyan betűk, amelyek tartalmazzák a bemenetet.
Ezeket a betűket a for ciklusban feltöltjük a foundletters változóban.
"""

def val(inputs, abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    found_letters = ""
    for letter in inputs:
        if letter in abc:
            found_letters += letter
    return found_letters


def main():
    print(val("Barking!"))
    print(val("KL754", "0123456789"))
    print(val("BEAN", "abcdefghijklmnopqrstuvwxyz"))


if __name__ == "__main__":
    main()
