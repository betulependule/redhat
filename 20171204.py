#! /usr/bin/env python3

cislo = 50


def odecitani(cislo):
    while cislo > 0:
        cislo = cislo - 2
        print(cislo)
    return(cislo)


odecitani(cislo)

seznam_cisel = [8, 13, 5, 6, 0, 10, 12]


def suda_licha(seznam_cisel):
    suda = 0
    licha = 0
    for x in seznam_cisel:
        if x % 2 == 0:
            suda = suda + 1
        else:
            licha = licha + 1
        return suda, licha


suda_licha(seznam_cisel)
