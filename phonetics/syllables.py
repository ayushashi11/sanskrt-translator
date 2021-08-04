import re
import itertools

vowels = 'aāiīuūeoṛḷṁṉ'
consonants = 'kgṅcjñṭḍṇtdnpbmyrlḻvśṣsh'
aspiratable_consonants = 'k|g|c|j|ṭ|ḍ|t|d|p|b'
glottal = '\u097D'
vowel_signs = '\u093E-\u094C\u093A-\u093B\u094E-\u094F\u0955-\u0957\u1CF8-\u1CF9'
nasals = '̇ṁ'
visarga = '\u0903'
nukta = '\u093C'
avagraha = '\u093D'
virama = '\u094D'
vedic_signs = '\u0304\u0323'
visarga_modifiers = '\u1CE2-\u1CE8'
combining = '\uA8E0-\uA8F1'
om = '\u0950'
accents = '\u0953-\u0954'
dandas = '\u0964-\u0965'
digits = '\u0966-\u096F'
abbreviation = '\u0970'
spacing = '\u0971'
vedic_nasals = '\uA8F2-\uA8F7\u1CE9-\u1CEC\u1CEE-\u1CF1'
fillers = '\uA8F8-\uA8F9'
caret = '\uA8FA'
headstroke = '\uA8FB'
space = '\u0020'
joiners = '\u200C-\u200D'
semivowels = "yrlv"

def syllabify(inputtext): 
    syllables = [] 
    curr = '' 
    # iterate over each character in the input. if a char belongs to a 
    # class that can be part of a syllable, then add it to the curr 
    # buffer. otherwise, output it to syllables[] right away. 
    for char in inputtext:
        print(curr)
        if re.match('[' + consonants + ']', char): 
            # if last in curr is not virama, output curr as syllable # else add present consonant to curr 
            # print("cons")
            if char=="h" and curr in aspiratable_consonants:
                curr = curr + char
            elif len(curr) > 0 and curr[-1] not in consonants: 
                syllables.append(curr) 
                curr = char
            elif len(curr) > 0 and (curr[-1] in consonants and char not in semivowels) and ((curr, char)!=("k","ṣ")):
                syllables[-1] += curr
                curr = char
            else: 
                curr = curr + char
        elif re.match('[' + vowels + ']', char): #+ avagraha + glottal + om + 
            # need to handle non-initial independent vowel letters, 
            # avagraha, and om 
            # print("vowel")
            if curr == '' and len(syllables) == 0:
                curr = char 
            elif curr == '': 
                syllables.append(curr) 
                curr = char 
            else: 
                curr = curr + char 
        elif re.match('[' + vowels + vedic_signs + ']', char): #+ visarga 
            #print("vowel")
            curr = curr + char
        elif re.match('[' + visarga_modifiers + ']', char):
            if len(curr) > 0 and curr[-1] == visarga: 
                curr = curr + char 
                syllables.append(curr) 
                curr = '' 
            else: 
                syllables.append(curr) 
                curr = '' 
        elif re.match('[' + nasals + vedic_nasals + ']', char): 
            # if last in curr is a vowel sign, output curr as syllable # else add present vowel modifier to curr and output as syllable 
            vowelsign = re.match('[' + vowels + ']$', curr)
            if vowelsign: 
                syllables.append(curr) 
                curr = '' 
            else: 
                curr = curr + char 
                syllables.append(curr) 
                curr = ''
        elif re.match('[' + nukta + ']', char): 
            curr = curr + char 
        elif re.match('[' + virama + ']', char): 
            curr = curr + char 
        elif re.match('[' + digits + ']', char): 
            curr = curr + char 
        elif re.match('[' + fillers + headstroke + ']', char): 
            syllables.append(char) 
        elif re.match('[' + joiners + ']', char): 
            curr = curr + char 
        else: 
            pass #print ("unhandled: " + char + " ") # handle remaining curr 
    if curr != '':
        if re.match('[' + vowels + ']', curr[-1]):
            syllables.append(curr) 
            curr = '' # return each syllable as item in a list
        else:
            syllables[-1] += curr
            curr = ''
    return syllables

def get_vowel(text: str):
    c = text.strip(consonants)
    return (c, text.index(c))

def get_nucleus(text):
    return text[:get_vowel(text)[1]]

def get_coda(text):
    c = get_vowel(text)
    return text[c[1]+(1 if c[0] != "" else 0):]
if __name__ == "__main__":
    print(get_coda("hṁk"))

    print(list(map(syllabify,"agnimīḻe purohitam yajñasya devaṁ ṛtvijam".split())))