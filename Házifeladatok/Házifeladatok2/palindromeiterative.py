#!/usr/bin/env python3

def palindrome(word):
    szokozep = len(word) // 2
    palindrome = True
    for i in range(0, szokozep):
        baloldal = word[i]
        jobboldal = word[len(word) - i - 1]
        if baloldal != jobboldal:
            palindrome = False
            break
    return palindrome


def main():
    print("Adj meg egy szót!")
    text = input()
    palindrome(text)
    if palindrome(text):
        print(f"A megadott szó: {text}, palindróma")
    else:
        print(f"A megadott szó: {text}, nem palindróma")

if __name__ == '__main__':
    main()