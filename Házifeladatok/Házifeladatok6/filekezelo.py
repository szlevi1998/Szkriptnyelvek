#!/usr/bin/env python3


def main():
    with open('string1.py', 'r') as input_file, open('cleared_string1.py', 'w') as output_file:
        for line in input_file:
            if not line.lstrip().startswith('#'):
                output_file.write(line)


if __name__ == "__main__":
    main()

