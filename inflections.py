def complete_sandhi(text):
    nt=""
    c=0
    while c<len(text)-1:
        if text[c]=='a':
            nt+="ा"
            c+=1
        elif text[c]=='b':
            nt=nt[:-1]
            c+=1 
        elif text[c:c+2]=='िi':
            nt+="ी"
            c+=2
        elif text[c:c+2]=='ुu':
            nt+="ू"
            c+=2
        elif text[c:c+2]=='ृo':
            nt+='रो'
            c+=2
        elif text[c:c+2]=='ृa':
            nt+='र्'
            c+=2
        elif text[c]=='A':
            nt+="स"
            c+=1
        elif text[c:c+2]=='िA':
            nt+="य"
            c+=2
        elif text[c:c+2]=='ुA':
            nt+="व"
            c+=2
        elif text[c:c+2]=='ृA':
            nt+='आर'
            c+=2
        else:
            nt+=text[c]
            c+=1
    return nt+text[-1]
def nsubj(ending, gender, number):
    #TODO: implement gender
    if ending=="a" or ending=="i" or ending=="u":
        if number=="sg":
            return "ः"
        elif number=="dual":
            return ending
        elif number=="pl":
            return "Aः"
    return ""
def dobj(ending, gender, number):
    #TODO: implement gender
    if number=="sg":
        return "म्"
    if ending=="a":
        return "aन्"
    elif ending=="i":
        return "iन्"
    elif ending=="u":
        return "uन्"
    return ""
def verb(ending, type, doer):
    if (ending, type, doer) == ("r","3a","i"):
        return "oमि"
    elif (ending, type, doer) == ("r","3a","we"):
        return "bुर्मः"
    elif (ending, type, doer) == ("r","3a","you"):
        return "oषि"
    elif (ending, type, doer) == ("r","3a","they"):
        return "bुर्वन्ति"
    elif (ending, type) == ("r","3a") and doer in ["he","she","it"]:
        return "oति"
    elif (ending, type, doer) == ("k","3a","i"):
        return "नोमि"
    elif (ending, type, doer) == ("k","3a","we"):
        return "नुमः"
    elif (ending, type, doer) == ("k","3a","they"):
        return "नुवन्ति"
    elif (ending, type, doer) == ("k","3a","you"):
        return "नोषि"
    elif (ending, type) == ("k","3a") and doer in ["he","she","it"]:
        return "नोति"
    elif (ending, type, doer) == ("r","3a","inf"):
        return "aतुम्"
    elif (ending, type, doer) == ("k","3a","inf"):
        return "तुम्"
    elif (type, doer) == ("1s","inf"):
        return "bितुम्"
    elif (type, doer) == ("1s","i"):
        return "bामि"
    elif (type, doer) == ("1s","we"):
        return "bामः"
    elif (type, doer) == ("1s","you"):
        return "bसि"
    elif (type, doer) == ("1s","they"):
        return "bथ"
    elif type == "1s" and doer in ["he","she","it"]:
        return "bति"
    return ""