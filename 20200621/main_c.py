# -*- coding: utf-8 -*-

import numpy as np

s = input()

x = np.base_repr(int(s), 26)

strings = {
"0": "a",
"1": "b",
"2": "c",
"3": "d",
"4": "e",
"5": "f",
"6": "g",
"7": "h",
"8": "i",
"9": "j",
"A": "k",
"B": "l",
"C": "m",
"D": "n",
"E": "o",
"F": "p",
"G": "q",
"H": "r",
"I": "s",
"J": "t",
"K": "u",
"L": "v",
"M": "w",
"N": "x",
"O": "y",
"P": "z",
}

strings_2 = {
"1": "a",
"2": "b",
"3": "c",
"4": "d",
"5": "e",
"6": "f",
"7": "g",
"8": "h",
"9": "i",
"A": "j",
"B": "k",
"C": "l",
"D": "m",
"E": "n",
"F": "o",
"G": "p",
"H": "q",
"I": "r",
"J": "s",
"K": "t",
"L": "u",
"M": "v",
"N": "w",
"O": "x",
"P": "y",
"Q": "z"
}

_index = 0
r = ''
for i in list(x):
    if _index == len(list(x)):
        r += strings[i]
    else:
        r += strings_2[i]
    _index += 1

print(r)
