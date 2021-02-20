#!/usr/bin/env/ python3

def hello(name,  color, what):
    #geza, kek az eg!
    #C-ben:
    # print f("%s, %s az %s!\n", name, color, what);
    # v1
    print(" 1) {0}, a {1} a {2} franchise történetének legjobb játékosa!".format(name.capitalize(),color,what))
    # v2
    #print(" 2) {}, {} az {}!".format(name, color, what))
    # v3
    #print(" 3) {nev}, {szin}, az {mi}!".format(nev = name, szin = color, mi = what))
    # v4
    #print(f"{name}, {color} az {what}!")

def main():
    hello("geza", "kek", "eg")
    print("-"* 40)
    hello("steph","Golden","Warriors")
##############################################

if __name__ == "__main__":
    main()