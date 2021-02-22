#!/usr/bin/env python3

def donuts(count):
    # TODO...
    if count >= 10:
        print('Sok')
    else:
        print("Fánkok száma: ", count)

    return


def both_ends(s):
    # TODO...

    if len(s) <= 2:
        print('')

    else:
        print(f"{s[0:2]}{s[-2:]}")

    return


def finding(s):
    s = "babble"
    s.find("b")


def main():
    donuts(8)
    both_ends("batman")
    finding("babble")

if __name__ == '__main__':
    main()
