#! /usr/bin/env python3

import string
abc = list(string.ascii_letters)
muj_list = [21, 4, 18, 4, 11, 4, 21, 0, 13, 14, 2, 4, 5000]


def divna_funkce(abc, muj_list):
    for x in muj_list:
        if x < len(abc):
            print(abc[x])


divna_funkce(abc, muj_list)
