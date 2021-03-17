#!/usr/bin/env python3

"""
Ebben a függvényben nézzük meg a számnak a számjegyeit.
Ifben azt nézzük a speciális esetet ha 0 a négyzet akkor 0-val bővítjük a digitet, ha más számjegy akkor a négyzetével.
Az utolsó ifben megnézzük,hogy ezeknek a számjegyek összegei megegyeznek az eredeti számmal.
"""


def munum(num):
    digit_pows = []
    for c in str(num):
        if c == '0':
            digit_pows.append(0)
        else:
            digit_pows.append(int(c) ** int(c))

    if (sum(digit_pows) == num):
        return True
    else:
        return False


"""
Itt a forciklussal rápróbálkozunk az összes számra 440 millióig.
"""

def main():
    mu_nums = []
    for i in range(0, 440000000):
        if munum(i):
            mu_nums.append(i)

    print(mu_nums)


if __name__ == "__main__":
    main()
