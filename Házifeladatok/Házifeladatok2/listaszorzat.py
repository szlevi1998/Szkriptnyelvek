#!/usr/bin/env python3

def listaszorzata():
    lista = [2, 2, 3, 4]

    szorzat = 1
    for x in lista:
        szorzat = szorzat * x
    return print('listának szorzata: ',szorzat)


def main():
    listaszorzata()


if __name__ == '__main__':
    main()
