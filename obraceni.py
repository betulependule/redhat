#! /usr/bin/env python3

argument = "pes"

def obraceni(argument):
	a = list(argument)
	a.reverse()
	b = "".join(a)
	print(b)


def cisla():
	for x in range(1, 99):
		if x % 2 == True:
			print(x)

cislice = [1, 1, 3, 2]
cislice_2 = []


def cisla_2(cislice, cislice_2):
	cislice.sort()
	y = min(cislice)
	for x in cislice:
		if x != y:
			cislice_2.append(x)
	print(min(cislice_2))
		


#obraceni(argument)
cisla_2(cislice, cislice_2)
