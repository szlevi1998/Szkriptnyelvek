#!/usr/bin/env python3

import math


def distance(p1, p2):
    magassag = p2[1] - p1[1]
    szelesseg = p2[0] - p1[0]
    tavolsag = magassag ** 2 + szelesseg ** 2
    tavolsag = math.sqrt(tavolsag)
    return tavolsag


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print('A ket pont kozti tavolsag:', distance(p1, p2))


#############################################################################

if __name__ == "__main__":
    main()
