from abc import ABC
from phonetics.syllables import get_vowel
class VerbSystem(ABC):
    
    def class1_present(v, pn):
        pass
    
    def class2_present(v, pn):
        pass
    
    def class3_present(v, pn):
        pass
    
    def class4_present(v, pn):
        pass
    
    def class5_present(v, pn):
        pass
    
    def class6_present(v, pn):
        pass
    
    def class7_present(v, pn):
        pass
    
    def class8_present(v, pn):
        pass
    
    def class9_present(v, pn):
        pass
    
    def class10_present(v, pn):
        pass
    
    def get_class_methods(class_, aorist):
        pass

class Parasmaipadi(VerbSystem):
    
    def class1_present(v, pn):
        ret = v.grade1
        if pn == "1s":
            ret += "ati"
        elif pn == "1d":
            ret += "ataḥ"
        elif pn == "1p":
            ret += "anti"
        elif pn == "2s":
            ret += "asi"
        elif pn == "2d":
            ret += "athaḥ"
        elif pn == "2p":
            ret += "atha"
        elif pn == "3s":
            ret += "āmi"
        elif pn == "3d":
            ret += "āvaḥ"
        elif pn == "3p":
            ret += "āmaḥ"
        return ret
    
    def class2_present(v, pn):
        ret = ""
        if pn == "1s":
            ret += v.grade1 + "ti"
        elif pn == "1d":
            ret += v.syllable + "taḥ"
        elif pn == "1p":
            ret += v.grade0 + "anti"
        elif pn == "2s":
            ret += v.grade1 + "si"
        elif pn == "2d":
            ret += v.syllable + "thaḥ"
        elif pn == "2p":
            ret += v.syllable + "tha"
        elif pn == "3s":
            ret += v.grade1 + "mi"
        elif pn == "3d":
            ret += v.syllable + "vaḥ"
        elif pn == "3p":
            ret += v.syllable + "maḥ"
        return ret
    
    def class3_present(v, pn):
        ret = v.cons + get_vowel(v.syllable)[0]
        if pn == "1s":
            ret += v.grade1 + "ti"
        elif pn == "1d":
            ret += v.syllable + "taḥ"
        elif pn == "1p":
            ret += v.grade0 + "anti"
        elif pn == "2s":
            ret += v.grade1 + "si"
        elif pn == "2d":
            ret += v.syllable + "thaḥ"
        elif pn == "2p":
            ret += v.syllable + "tha"
        elif pn == "3s":
            ret += v.grade1 + "mi"
        elif pn == "3d":
            ret += v.syllable+ "vaḥ"
        elif pn == "3p":
            ret += v.syllable + "maḥ"
        return ret
    
    def get_class_methods(class_, aorist):
        if class_ == 1:
            return [Parasmaipadi.class1_present]
        elif class_ == 2:
            return [Parasmaipadi.class2_present]
        else:
            return [Parasmaipadi.class3_present]