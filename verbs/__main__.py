from phonetics.grades import grade2
from . import Verb

paṭh = Verb("paṭh")
gṁ = Verb("gṁ", prefixes=["ava"]) #, first_grade="gacch", second_grade="gacch"
hṉ = Verb("hṉ", class_=3, zero_grade="ghṉ")

#print(paṭh.grade0, paṭh.grade1, paṭh.grade2)
#print(gṁ.grade0, gṁ.grade1, gṁ.grade2)

print(paṭh.present("3s"))
print(gṁ.present("2d"))
print(hṉ.present("1p"))
