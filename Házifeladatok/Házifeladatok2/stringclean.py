#!/usr/bin/env python3

def clean(address):
    hugo = address.replace("\n", '')

    if "\n" in address:
        print("The new IP: ", hugo)
    else:
        print("The same IP: ", address)


def main():
    clean("192.20.246.138:\n 6666")


if __name__ == '__main__':
    main()
