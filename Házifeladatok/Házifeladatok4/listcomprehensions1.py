#!/usr/bin/env python3

def ex_1():
    list_of_words = ['auto', 'villamos', 'metro']
    result = [w.upper() + '!' for w in list_of_words]
    print(result)


def ex_2():
    list_of_names = ['aladar', 'bela', 'cecil']
    result = [w.capitalize() for w in list_of_names]
    print(result)


def ex_3():
    result = [0 for n in range(10)]
    print(result)


def ex_4():
    numbers = list(range(0, 10 + 1))
    result = [n * 2 for n in numbers]
    print(result)


def ex_5():
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    result = [n.strip() for n in numbers]
    print(result)


def ex_6():
    input_number = "1234567"
    result = [int(i) for i in input_number]
    print(result)


def ex_7():
    sentence = 'The quick brown fox jumps over the lazy dog'
    result = [len(s) for s in sentence.split()]
    print(result)


def ex_8():
    sentence = "python is an awesome language"
    result = [s for s in sentence.split()]
    print(result)


def ex_9():
    sentence = "The quick brown fox jumps over the lazy dog"
    result = [(str(s), len(s)) for s in sentence.split()]
    print(result)


def ex_10():
    numbers = list(range(0, 10))
    result = [i for i in numbers if i % 10 == 0]
    print(result)


def ex_11():
    numbers = list(range(0, 20))
    result = [i ** 2 for i in numbers if i % 2 == 0]
    print(result)


def ex_12():
    numbers = list(range(0, 20))
    result = [i ** 2 for i in numbers if i*i % 10 == 4]
    print(result)


def ex_13():
    result = "".join(chr(num) for num in range(65, 90+1))
    print(result)


def ex_14():
    input_words = [' apple ', ' banana ', ' kiwi']
    result = [str(w.strip()) for w in input_words]
    print(result)


def ex_15():
    numbers = [1, 0, 1, 1, 0, 1, 0, 0]
    result = ["".join(str(l) for l in numbers)]
    print(result)


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_4()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()
    ex_10()
    ex_11()
    ex_12()
    ex_13()
    ex_14()
    ex_15()


if __name__ == "__main__":
    main()
