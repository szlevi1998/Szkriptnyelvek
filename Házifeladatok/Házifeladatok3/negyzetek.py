#!/usr/bin/env python3

def squares(start, end):
    return [i ** 2 for i in range(start, end + 1)]


def main():
    a = sum(range(0, 101))
    osszegnegyzet = a ** 2
    sumofsquares = sum(squares(1, 100))

    print("this thing", osszegnegyzet - sumofsquares)


if __name__ == '__main__':
    main()
