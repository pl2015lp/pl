print '\n>> task 1 <<'
import nltk
from nltk.corpus import wordnet as wn
a=wn.synset('country.n.02').member_meronyms()
print a
b=wn.synset('table.n.02').part_meronyms()
print b
c=wn.synset('water.n.01').substance_meronyms()
print c
a2=wn.synset('copilot.n.01').member_holonyms()

print '\n>> task 3 <<'
names=nltk.corpus.names
cfd=nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
p=cfd.plot()
print p

print '\n>> task 4 <<'


