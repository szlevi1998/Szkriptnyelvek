#!/usr/bin/env python3

def main():
    megadott_szo = ["zsa"]
    magas_mgh = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]
    mely_mgh = ["a", "á", "o", "ó", "u", "ú"]

    if magas_mgh in megadott_szo:
        return "A megadott szó vegyes"

    else:
        return "A megadott szó nem vegyes"


if __name__ == '__main__':
    main()
