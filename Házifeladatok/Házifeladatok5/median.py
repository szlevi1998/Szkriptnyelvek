#!/usr/bin/env python3

def median(firstlist):
    halmaz = sorted(firstlist)
    halmaz_length = len(halmaz)
    halmaz_half = (halmaz_length - 1) // 2

    if halmaz_length % 2:
        print(halmaz[halmaz_half])
    else:
        print((halmaz[halmaz_half] + halmaz[halmaz_half + 1]) / 2)


def main():
    median([1, 2, 3, 4, 5])
    median([3, 1, 2, 5, 3])
    median([1, 300, 2, 200, 1])
    median([3, 6, 20, 99, 10, 15])

if __name__ == "__main__":
    main()
