from nltk import wordpunct_tokenize
from nltk import WordNetLemmatizer
from nltk import sent_tokenize
from nltk import pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet
import string
import re    
import nltk
from nltk.corpus import stopwords

stoplist = set(stopwords.words("english"))


replacement_patterns = [  
    (r'won\'t', 'will not'),  
    (r'can\'t', 'cannot'),  
    (r'i\'m', 'i am'),  
    (r'ain\'t', 'is not'),  
    (r'(\w+)\'ll', '\g<1> will'),  
    (r'(\w+)n\'t', '\g<1> not'),  
    (r'(\w+)\'ve', '\g<1> have'),  
    (r'(\w+)\'s', '\g<1> is'),  
    (r'(\w+)\'re', '\g<1> are'),  
    (r'(\w+)\'d', '\g<1> would')
]

class RegexpReplacer(object):  
    def __init__(self, patterns=replacement_patterns):    
        self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]  
        
    def replace(self, text):    
        s = text    
        for (pattern, repl) in self.patterns:      
            s = re.sub(pattern, repl, s)    
        return s

class AntonymReplacer(object):
    
    def replace(self, word, pos=None):
        antonyms = set()
        for syn in wordnet.synsets(word, pos=pos):
            for lemma in syn.lemmas():
                for antonym in lemma.antonyms():
                    antonyms.add(antonym.name())
        if len(antonyms) > 0:
            ans = antonyms.pop()            
            return ans
        else:
            return None
        
    def replace_negations(self, sent):
        i, l = 0, len(sent)
        words = []
        while i < l:
            word = sent[i]
            if word == 'not' and i+1 < l:
                ant = self.replace(sent[i+1])
                if ant:
                    words.append(ant)
                    i += 2
                    continue
            words.append(word)
            i += 1
        return words


class Remove_Noise(object):
    
    def __init__(self,stop_word = stoplist):
        self.stop_word = stoplist
    
    def noise_rm(self,doc):
        doc = re.sub('[#$%^&\',:()*+/<=>@[\\]^_``{|}~]',' ',doc)
        doc = re.sub('[0-9]+',' ',doc)
        doc = re.sub('\n','',doc)
        doc = re.sub(' +',' ',doc)
        doc = doc.lower()
        return doc
    
    def lemmatize(self,token, tag):
        tag = {
            'N': wn.NOUN,
            'V': wn.VERB,
            'R': wn.ADV,
            'J': wn.ADJ
        }.get(tag[0], wn.NOUN)
        lemmatizer = WordNetLemmatizer()
        return lemmatizer.lemmatize(token, tag)
    
    def tokenize(self,document): 
        #document = unicode(document,'utf-8')
        lemmy = []
        for sent in sent_tokenize(document):
            for token, tag in pos_tag(wordpunct_tokenize(sent)):
                
                lemma = self.lemmatize(token, tag)
                lemmy.append(lemma)
        return lemmy


replacer = RegexpReplacer()
remover = Remove_Noise()
AntoRep = AntonymReplacer()

def join_tokens(data):
    ans = ' '.join(data)
    return ans


def process(text):
    replacer = RegexpReplacer()
    remover = Remove_Noise()
    AntoRep = AntonymReplacer()
    text = replacer.replace(text)
    text = remover.noise_rm(text)
    text = remover.tokenize(text)
    text = AntoRep.replace_negations(text)
    text = join_tokens(text)
    return text


