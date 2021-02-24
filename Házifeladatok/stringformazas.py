#!/usr/bin/env python3

def main():
    # Multiple Substitution Values
    string1 = "vengeance"
    string2 = "the night"
    string3 = "Batman"

    string4 = "I am  {}, I am {}, I am {}! ".format(string1, string2, string3)

    print(string4)
    print("-" * 54)

    # data for the Golden State Warriors against the New York Knicks on 23rd February 2021
    # data

    print(" Golden State Warriors team stats against the New York Knicks on 23rd February 2021")

    starters = [

        ['Stephen Curry', 'PG', 37, 6, 6, 9, 22, 41],
        ['Kelly Oubre', 'SG', 19, 8, 2, 8, 18, 44],
        ['Andrew Wiggins', 'SF', 16, 5, 1, 6, 13, 46],
        ['Draymond Green', 'PF', 7, 9, 12, 3, 9, 33],
        ['Kevon Looney', 'C', 2, 6, 4, 1, 1, 100],
        ['Kent Bazemore', 'SG', 9, 0, 1, 3, 7, 43],
        ['James Wiseman', 'C', 14, 2, 1, 6, 9, 67],
        ['Eric Paschall', 'PF', 8, 1, 1, 3, 6, 50],
        ['Brad Wanamaker', 'PG', 2, 1, 2, 1, 2, 50],
        ['Damion Lee', 'SF', 0, 3, 0, 0, 2, 0],
        ['Team Overall', 'NA', 114, 41, 30, 40, 89, 45]
    ]

    # define format row
    row = "| {player:<16s} | {position:<2s} | {pts:3d}| {reb:2d} | {ast:2d}  | {fgm:2d} | {fga:2d} |{fgp:3d}".format

    for p in starters:
        print(row(player=p[0], position=p[1], pts=p[2], reb=p[3], ast=p[4], fgm=p[5], fga=p[6], fgp=p[7]))


if __name__ == '__main__':
    main()
    input()
