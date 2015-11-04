from __future__ import division
import nltk, re, pprint


import urllib, nltk
from urllib import urlopen

print '========= Task 1 ========='
link = "http://www.nltk.org/"
data = urlopen(link).read()
raw = nltk.clean_html(data)
t = nltk.word_tokenize(raw)
print 'Text of loaded and parssed url: \n', t[:30]
################################################################
print '\n ========= Task 2 ========='
def Mytext (t):
    w=''
    for line in t:
        a=line.strip()
        str=a
    return str
f= open ('E:\Text\corpus.txt')
text=f.read()
################################################################print text

print '\n ========= Task 3 ========='
sent = ['The', 'dog', 'gave', 'John', 'the','newspaper']
result=[(word, len(word)) for word in sent]
print result
################################################################

print '\n ========= Task 4 ========='
a="3"
print 'The first case: "3" * 7 =', a*7
print 'The second case: 3 * 7 =', 3*7
print 'Conversation int("3") =', int("3")
print 'Conversation str(3) =' , str(3)
################################################################
print '\n ========= Task 5 ========='
print '6 spaces before:','%6s' % 'str'
print '6 spaces after:','%-6s' % 'str'

################################################################

print '\n ========= Task 7 ========='

file = open('E:\doc.txt')
p=file.readlines()
print p
a=[]
for i in p:
    c=i.split()
    a.append([i.split()[0],int(i.split()[1])])
################################################################
print '\n ========= Task 10 ========='
import random
aa=''
for i in range(500):
    aa=aa+''.join(random.choice("aehh "))
print  aa[:50]
bb=aa.split()
print bb[:15]

################################################################
print '\n ========= Task 13 ========='

import nltk
nltk.corpus.gutenberg.fileids()
nltk.download()
way = nltk.data.find('corpora/gutenberg/austen-sense.txt')
raw = open(way).read()
tokens = nltk.word_tokenize(raw[:300])
print 'Text of loaded and parssed url: \n', raw[:300], '\n'
porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
print [porter.stem(t) for t in tokens], '\n'
print [lancaster.stem(t) for t in tokens]
################################################################
print '\n ========= Task 14 ========='

from nltk.corpus import abc
l=0
n=0
for w in nltk.corpus.abc.words():
    l+=len(w)
    n+=1
    mw = l/n #середня к-сть літер у слові
print mw
ms = len(nltk.corpus.abc.words()) / len(nltk.corpus.abc.sents())#середнє значення к-сті слів у реченні в тексті 
print ms
ari = 4.71*mw+0.5*ms-21.43# визначаю міру оцінки читабельності за цим виразом
print '\n ARI-Automated Readibility Index'
print ari

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.abc.raw('rural.txt')
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[11:13])

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.abc.raw('science.txt')
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[11:13])







