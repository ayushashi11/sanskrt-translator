import re
from .syllables import get_coda, get_vowel, get_nucleus, consonants


def grade1(syllable):
    vowel = get_vowel(syllable)[0]
    if vowel == "ṁ":
        vowel = "aṁ"
    elif vowel == "ṉ":
        vowel = "aṉ"
    elif vowel in ("ṛ", "ṝ"):
        vowel = "ar"
    elif vowel in ("ḷ","ḹ"):
        vowel = "al"
    elif vowel in ("i", "ī"):
        vowel = "e"
    elif vowel in ("u","ū"):
        vowel = "o"
    elif vowel == "":
        vowel = "a"
    return get_nucleus(syllable) + vowel + get_coda(syllable)

def grade2(syllable):
    vowel = get_vowel(syllable)[0]
    if vowel == "ṁ":
        vowel = "āṁ"
    elif vowel == "ṉ":
        vowel = "āṉ"
    elif vowel in ("ṛ", "ṝ"):
        vowel = "ār"
    elif vowel in ("ḷ","ḹ"):
        vowel = "āl"
    elif vowel in ("i", "ī"):
        vowel = "ai"
    elif vowel in ("u","ū"):
        vowel = "au"
    elif vowel in ("", "a"):
        vowel = "ā"
    return get_nucleus(syllable) + vowel + get_coda(syllable)

def consograde1(syllable):
    conso = get_nucleus(syllable)
    if len(conso) == 0:
        return ""
    conso = conso[0] + ("h" if len(conso) > 1 and conso[1] == "h" else "")
    if conso in ["k","kh"]:
        return "c"
    elif conso in ["g", "gh", "h"]:
        return "j"
    elif conso == "ch":
        return "c"
    elif conso == "jh":
        return "j"
    elif conso == "ṭh":
        return "ṭ"
    elif conso == "ḍh":
        return "ḍ"
    elif conso == "th":
        return "t"
    elif conso == "dh":
        return "d"
    elif conso == "ph":
        return "p"
    elif conso == "bh":
        return "b"
    else:
        return conso

if __name__ == '__main__':
    for syllable in ["kḷp","hṁ", "gam", "kṛ", "hiṣ", "ṣṭhā", "nam", "s", "d", "vid"]:
        print(f"\x1b[38;2;254;69;69m{syllable}\x1b[0m")
        print(consograde1(syllable))
        print(grade1(syllable))
        print(grade2(syllable))
