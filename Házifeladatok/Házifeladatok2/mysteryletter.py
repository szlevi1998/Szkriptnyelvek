#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""


def my_replace(text_to_modify):
    text_to_modify = text_to_modify.replace("1", "I")
    text_to_modify = text_to_modify.replace("3", "E")
    text_to_modify = text_to_modify.replace("4", "A")
    text_to_modify = text_to_modify.replace("5", "S")
    text_to_modify = text_to_modify.replace("7", "T")
    return text_to_modify


def main():
    print(my_replace(TEXT))


##############################################################################

if __name__ == "__main__":
    main()
