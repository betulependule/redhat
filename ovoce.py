#! /usr/bin/env python3

ovoce = dict(jablko="zelena", hruska="zluta", pomeranc="oranzovy",
             svestka="modra", tresen="cervena")

for i in ovoce:
    print(i)

for i in ovoce.values():
    print(i)

for i in ovoce.items():
    print(i)

while ovoce:
    plodina, barva = ovoce.popitem()
    print("{}:{}".format(plodina, barva))
