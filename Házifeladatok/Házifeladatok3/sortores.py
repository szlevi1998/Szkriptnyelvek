import sys
import random as r

UPTO = 100


def main():
    for i in range(UPTO):
        print(r.randint(0, 9), end="")
    print(UPTO)


if __name__ == '__main__':
    main()
