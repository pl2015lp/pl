
"\n<<<task 1>>>"
from __future__ import division
import nltk
nltk.corpus.gutenberg.fileids()

token1=nltk.corpus.gutenberg.words('austen-persuasion.txt')
print "\nNumber of tokens in austen-persuasion:"
t=len(token1)
print t
print "\nNumber of type in austen-persuasion:"
types=len(set(token1))
print types

"\n<<<task 5>>>"
from nltk.corpus import brown
from nltk.probability import *
print brown.categories()
cfd=nltk.ConditionalFreqDist((genre,word)
   for genre in brown.categories()
       for word in brown.words(categories=genre))
genres=['news','government']
f = brown.words()
f = FreqDist(f)
w=f.keys()
synonyms=['assess','evaluate','rate']
pronouns=['he','him','myself','their','it']
print "\ncompare key_words in two genres:"
cfd.tabulate(conditions=genres,samples=(w[:10]))
print "\ncompare synonyms in two genres:"
cfd.tabulate(conditions=genres,samples=synonyms)
print "\ncompare pronouns in two genres:"
cfd.tabulate(conditions=genres,samples=pronounsprint "n\>> task 7 <<"

cfd=nltk.ConditionalFreqDist((genre,word)
   for genre in brown.categories()
       for word in brown.words(categories=genre))
f = brown.words()
n = FreqDist(f)
number = sorted([w for w in set(f) if  n[w] >= 3])
print '\nWords thar appear not less than 3 times are:'
print number

print "n\>> task 9 <<"
from nltk.corpus import stopwords

text1=nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
f = FreqDist([w.lower() for w in text1])
v=f.keys()
ex=stopwords.words('english')
a= []
for w in v:
    if (len(w) >2 and (w in v)!= (w in ex)):
        a.append(w)
print '\n50 most frequent words without meaningless words:'
print a[:50]

print '\n>> task 8 <<'
import nltk
from nltk.corpus import brown
from nltk.probability import *

from tabulate import tabulate
print tabulate(table, headers=["Relation", "Genres"])

for category in brown.categories():
#for fileid in brown.fileids():
   num_words = len(brown.words(categories=category))
   num_vocab = len(set([w.lower() for w in brown.words(categories=category)]))
   print round (num_words/num_vocab,2), category

print '\n>> task 13 <<'
from nltk.book import text4

def hedge(t):
   count=0
   res=""   
   for w in t:
      if count < 1:
         res+=w+" "
         count += 1
      else:
         count=0
         res += "like "+w+" "
   return res
new=hedge(text4[51:95])
print new


