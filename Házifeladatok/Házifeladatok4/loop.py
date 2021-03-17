#!/usr/bin/env python3

def loop(num, debug=False):
    if debug == False:
        for e in range(1, num + 1):
            print(e, end=" ")
        print()
    elif debug == True:
        print("# A ciklus eleje: ")
        for e in range(1, num + 1):
            print(e, end=" ")
        print()
        print("# A ciklus vége.")


def main():
    loop(5)
    loop(5, debug=True)


if __name__ == "__main__":
    main()
