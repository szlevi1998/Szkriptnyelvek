#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) < 3: 
        print("Kevés a megadott argumentum száma!, a fordítás menete ./osszeadasargu.py a b")

    else:
    
        a = sys.argv[1]
        b = sys.argv[2]
        eredmeny = int(a) + int(b)
        print("A megadott számok összege: ", eredmeny)


if __name__ == '_main_':
    main()
