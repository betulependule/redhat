#! /usr/bin/env python3

def bum_bac():
	cislo1=int(input("Napiste prvni libovolne cislo: "))
	cislo2=int(input("Napiste druhe libovolne cislo: "))
	posloupnost=range(cislo1,cislo2,1)
	a="bum"
	b="bac"
	for posloupnost in range(cislo1,cislo2,1):
		if posloupnost%2==0 and posloupnost%6==0:
			print(a+b)
		elif posloupnost%6==0:
			print(b)
		elif posloupnost%2==0:
			print(a)		
		else:
			print(posloupnost)
bum_bac()
		
