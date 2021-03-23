#!/usr/bin/env python3

input_text ="""
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
"""

def ekezet_eltavolitas(ekezet_replace):
    ekezet_replace = ekezet_replace.replace("á", "a")
    ekezet_replace = ekezet_replace.replace("Á", "A")
    ekezet_replace = ekezet_replace.replace("é", "e")
    ekezet_replace = ekezet_replace.replace("É", "é")
    ekezet_replace = ekezet_replace.replace("í", "i")
    ekezet_replace = ekezet_replace.replace("Í", "I")
    ekezet_replace = ekezet_replace.replace("ó", "o")
    ekezet_replace = ekezet_replace.replace("Ó", "O")
    ekezet_replace = ekezet_replace.replace("ö", "o")
    ekezet_replace = ekezet_replace.replace("Ö", "O")
    ekezet_replace = ekezet_replace.replace("ő", "o")
    ekezet_replace = ekezet_replace.replace("Ő", "O")
    ekezet_replace = ekezet_replace.replace("ú", "u")
    ekezet_replace = ekezet_replace.replace("Ú", "U")
    ekezet_replace = ekezet_replace.replace("ü", "u")
    ekezet_replace = ekezet_replace.replace("Ü", "u")
    ekezet_replace = ekezet_replace.replace("ű", "u")
    ekezet_replace = ekezet_replace.replace("Ű", "u")
    return ekezet_replace


def main():
    print(ekezet_eltavolitas(input_text))


if __name__ == "__main__":
    main()
