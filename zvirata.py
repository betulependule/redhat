#! /usr/bin/env python3

zvirata = {"jelen":4, "pavouk":8, "husa":2, "kralik":4, "krava":4, "zajic":4, "had":0,"clovek":2, "aligator":4, "orel":2}
ctyrnozi = []

for key, value in zvirata.items():
	if value>=4:
		ctyrnozi.append(key)
	else:
		pass
print("Mezi crytnoha zvirata patri: {}".format(ctyrnozi))
		
lepsi_zvirata = {"jelen":{"srst":"chlupy", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "pavouk":{"srst":"chlupy", "pocet_nohou":"0", "pocet_oci":"8", "ocas":"ne"}, "husa":{"srst":"peri", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "kralik":{"srst":"chlupy", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "krava":{"srst":"chlupy", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "zajic":{"srst":"chlupy", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "had":{"srst":"supiny", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "clovek":{"srst":"chlupy??", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"bohuzel_ne"}, "aligator":{"srst":"supiny", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}, "orel":{"srst":"peri", "pocet_nohou":"0", "pocet_oci":"2", "ocas":"ano"}}

kolo=1

def balik_nohou(zvirata, lepsi_zvirata, kolo):
	for i in lepsi_zvirata.values():
		for key, value in i.items():
			if key=="pocet_nohou" and kolo==2:
				i["pocet_nohou"]=zvirata["pavouk"]
				kolo=kolo+1
			elif key=="pocet_nohou" and (kolo==3 or kolo==8 or kolo==10):
				i["pocet_nohou"]=zvirata["husa"]
				kolo=kolo+1
			elif key=="pocet_nohou" and kolo==7:
				i["pocet_nohou"]=zvirata["had"]
				kolo=kolo+1
			elif key=="pocet_nohou":
				i["pocet_nohou"]=zvirata["jelen"]
				kolo=kolo+1
			else:
				pass
	print(lepsi_zvirata)

balik_nohou(zvirata, lepsi_zvirata, kolo)

kolo=1

nechlupati_s_ocasy = []


for i in lepsi_zvirata:
	if kolo==3:
		nechlupati_s_ocasy.append("husa")
		kolo=kolo+1
	elif kolo==7:
		nechlupati_s_ocasy.append("had")
		kolo=kolo+1
	elif kolo==9:
		nechlupati_s_ocasy.append("aligator")
		kolo=kolo+1
	elif kolo==10:
		nechlupati_s_ocasy.append("orel")
		kolo=kolo+1
	else:
		kolo=kolo+1

print("Zvirata s ocasy bez chlupu jsou: {}".format(nechlupati_s_ocasy))


