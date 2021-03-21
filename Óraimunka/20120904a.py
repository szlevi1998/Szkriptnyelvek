#!/usr/bin/env python3

def main():
    the_list = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    converter = set(the_list)
    sorted_list = sorted(converter)
    print(sorted_list)
    print(type(sorted_list))


if __name__ == '__main__':
    main()
