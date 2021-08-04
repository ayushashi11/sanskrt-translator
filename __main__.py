import spacy
from data import *
from inflections import *
import flask
app = flask.Flask(__name__)
nlp=spacy.load("en_core_web_sm")
tex="we are studying"
doc = nlp(tex)
subjects = []
text = []
print("\x1b[38;2;255;150;150m[ translating ]\x1b[0m ",tex)
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_)
    continue
    if token.pos_=="PRON":
        if token.dep_=="nsubj":
            subjects.append(token.lemma_)
            text.append(pronouns[token.lemma_.lower()][0])
        elif token.dep_=="dobj":
            text.append(pronouns[token.lemma_.lower()][1])
    elif token.pos_=="VERB" and token.tag_=="VBP":
        print(token.morph)
        sub = subjects.pop().lower()
        verb_data = verbs[token.lemma_.lower()]
        inflec = verb(verb_data[1], verb_data[2], sub)
        print(verb_data, sub, inflec)
        text.append(verb_data[0]+inflec)
    elif token.pos_=="VERB" and token.tag_=="VB":
        sub = "inf"
        print(token.morph)
        verb_data = verbs[token.lemma_.lower()]
        inflec = verb(verb_data[1], verb_data[2], sub)
        print(verb_data, sub, inflec)
        text.append(verb_data[0]+inflec)
    elif token.pos_=="VERB" and token.tag_=="VBG":
        sub = "inf"
        print(token.morph)
        verb_data = verbs[token.lemma_.lower()]
        inflec = verb(verb_data[1], verb_data[2], sub)
        print(verb_data, sub, inflec)
        text.append(verb_data[0]+inflec)
    elif token.pos_=="AUX" and token.tag_=="MD":
        sub = subjects.pop().lower()
        print(token.morph)
        verb_data = verbs[token.lemma_.lower()]
        inflec = verb(verb_data[1], verb_data[2], sub)
        print(verb_data, sub, inflec)
        text.append(verb_data[0]+inflec)
    elif token.pos_=="NOUN":
        if token.dep_=="nsubj":
            subjects.append("it")
            noun_data=nouns[token.lemma_.lower()]
            number = "sg"
            if token.tag_=="NNS":
                number = "pl"
            text.append(noun_data[0]+nsubj(noun_data[1],noun_data[2],number))
        elif token.dep_=="dobj":
            noun_data=nouns[token.lemma_.lower()]
            number = "sg"
            if token.tag_=="NNS":
                number = "pl"
            text.append(noun_data[0]+dobj(noun_data[1],noun_data[2],number))
    elif token.text=="to" and token.dep_=="aux":
        pass
    else:
        text.append(token.text)
print("\x1b[38;2;150;255;150m[ result ]\x1b[0m ",)#list(complete_sandhi(' '.join(text))))
#@app.route('/api')
#def api():
#    return flask.jsonify(tex=complete_sandhi(text))
#@app.route('/')
#def index():
#    return """
#<script>
#fetch('/api').then((data)=>{
#    return data.json()
#}).then((data)=>{
#    document.write(data["tex"])
#});
#</script>
#    """
#
#app.run()
#