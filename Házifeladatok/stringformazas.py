#!/usr/bin/env python3

def main():
    # Multiple Substitution Values
    string1 = "vengeance"
    string2 = "the night"
    string3 = "Batman"

    string4 = "I am  {}, I am {}, I am {}! ".format(string1,string2,string3)

    print(string4)

    # data for the CURRENT Golden State Warriors starters
    # data
    starters = [
        ['Andre Iguodala', 4, 3, 7],
        ['Klay Thompson', 5, 0, 21],
        ['Stephen Curry', 5, 8, 36],
        ['Draymond Green', 9, 4, 11],
        ['Andrew Bogut', 3, 0, 2],
    ]

    # define format row
    row = "| {player:<16s} | {reb:2d} | {ast:2d} | {pts:2d} |".format

    for p in starters:
        print(row(player=p[0], reb=p[1], ast=p[2], pts=p[3]))


if __name__ == '__main__':
        main()
        input()
