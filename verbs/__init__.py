from phonetics.grades import grade1, grade2, consograde1
from .inflections import Parasmaipadi
from phonetics.sandhi import complete_sandhi
class Verb:
    def __init__(self, syllable, class_=1, type_="ps_", zero_grade = None, first_grade = None, second_grade = None, prefixes = [], extras=[], **kwargs) -> None:
        self.syllable = syllable
        self.grade0 = zero_grade or (syllable)
        self.grade1 = first_grade or grade1(syllable)
        self.grade2 = second_grade or grade2(syllable)
        self.cons = consograde1(syllable)
        self.prefixes = prefixes
        self.extras = extras
        self.class_ = class_
        self.type = type_
        self.kwargs = kwargs
        fns = Parasmaipadi.get_class_methods(class_, type_[1:3])
        self.__present = kwargs.get("presentfn", None) or fns[0]
    
    def present(self, pn):
        return ' '.join(self.extras) + (' ' if len(self.extras)>0 else '') + complete_sandhi(''.join(self.prefixes) + (self.kwargs.get("present"+pn, None) or self.__present(self,pn)))
