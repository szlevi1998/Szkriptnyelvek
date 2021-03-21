#!/usr/bin/env python3

def main():
    blank_dictionary = {}
    some_list = [2, 5, 6]
    some_list[0] = 20
    blank_dictionary['a'] = 'alfa'
    blank_dictionary['b'] = 'beta'
    blank_dictionary['o'] = 'omega'
    blank_dictionary['g'] = 'gamma'
    result = blank_dictionary.get('x', 'that aint it')
    blank_dictionary['a'] = 'ALFA'
    keys_of_the_dictionary = blank_dictionary.keys()
    values_of_the_dictionary = blank_dictionary.values()
    for k in sorted(blank_dictionary.keys()):
        print(k, '->', blank_dictionary[k])

    print("-" * 30)

    for k, v in blank_dictionary.items():
        print(k, '->', v)

    del blank_dictionary['a']
    print("-" * 20)
    print(blank_dictionary)


if __name__ == '__main__':
    main()
