# a program lényege a következő: az inputnak megadott szám után megadja a megfelelő angol végződést
# például: 1st 2nd 3rd 4th stb.

def main():
    print("Give me a number")

    szam = str(input())

    if szam.endswith("1"):
        print("You are ", szam, "st")
    elif szam.endswith("2"):
        print("You are ", szam, "nd")
    elif szam.endswith("3"):
        print("You are ", szam, "rd")
    else:
        print("You are ", szam, 'th')


if __name__ == '__main__':
    main()
