from phonetics.grades import grade2
from . import Verb

paṭh = Verb("paṭh")
gṁ = Verb("gṁ", prefixes=["ava"]) #, first_grade="gacch", second_grade="gacch"
hṉ = Verb("hṉ", class_=2, zero_grade="ghṉ")
s = Verb("s", class_=2)
ad = Verb("ad", class_=2)
vac = Verb("vac", class_=2, extras=["iha"])
hu = Verb("hu", class_=3)

#print(paṭh.grade0, paṭh.grade1, paṭh.grade2)
#print(gṁ.grade0, gṁ.grade1, gṁ.grade2)

print(paṭh.present("1s"), paṭh.present("1d"), paṭh.present("1p"), paṭh.present("2s"), paṭh.present("2d"), paṭh.present("2p"), paṭh.present("3s"), paṭh.present("3d"), paṭh.present("3p"))
print(gṁ.present("1s"), gṁ.present("1d"), gṁ.present("1p"), gṁ.present("2s"), gṁ.present("2d"), gṁ.present("2p"), gṁ.present("3s"), gṁ.present("3d"), gṁ.present("3p"))
print(hṉ.present("1s"), hṉ.present("1d"), hṉ.present("1p"), hṉ.present("2s"), hṉ.present("2d"), hṉ.present("2p"), hṉ.present("3s"), hṉ.present("3d"), hṉ.present("3p"))
print(s.present("1s"), s.present("1d"), s.present("1p"), s.present("2s"), s.present("2d"), s.present("2p"), s.present("3s"), s.present("3d"), s.present("3p"))
print(ad.present("1s"), ad.present("1d"), ad.present("1p"), ad.present("2s"), ad.present("2d"), ad.present("2p"), ad.present("3s"), ad.present("3d"), ad.present("3p"))
print(vac.present("1s"), vac.present("1d"), vac.present("1p"), vac.present("2s"), vac.present("2d"), vac.present("2p"), vac.present("3s"), vac.present("3d"), vac.present("3p"))
print(hu.present("1s"), hu.present("1d"), hu.present("1p"), hu.present("2s"), hu.present("2d"), hu.present("2p"), hu.present("3s"), hu.present("3d"), hu.present("3p"))
