from __future__ import division
print '\n>> task 1 <<'
import nltk
from nltk.book import *
from nltk.corpus import wordnet as wn

a=wn.synset('country.n.02').member_meronyms()
print a
b=wn.synset('table.n.02').part_meronyms()
print b
c=wn.synset('water.n.01').substance_meronyms()
print c
a2=wn.synset('copilot.n.01').member_holonyms()
print a2
b2=wn.synset('course.n.07').part_holonyms()
print b2
c2=wn.synset('gin.n.01').substance_holonyms()
print c2

print '\n>> task 3 <<'
names=nltk.corpus.names
cfd=nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
p=cfd.plot()
print p

print '\n>> task 4 <<'


entries=nltk.corpus.cmudict.entries()
print len(entries)
w=[]
p=[]
for word,pron in entries:
    w.append(word)
    p.append(pron)

print len(word)


print '\n>> task 7 <<'
import random
snt=text1
print 'My text: ', snt,'.\n'
rnd=[]
for i in range(15):
    rnd.append(random.choice(snt))
print rnd

print '\n>> task 10 <<'

# øóêàş âñ³ ³ìåííèêè ç wn
ns=[]

for i in wn.all_synsets('n'):
    for j in i.lemma_names:
        ns.append(j) #â ñïèñêó ç³áğàí³ âñ³ ³ìåíà ëåì (âñ³ ³ìåííèêè àëå ç ïîâòîğàìè)
num=len(set(ns))#ê³ëüê³ñòü ³ìåííèê³â ó WN
print num
q=0
for i in set(ns):  # ïåğåáèğàş âñ³ ³ìåííèêè
    q=q+len(wn.synsets(i,'n'))  # ñóìóş çíà÷åííÿ ³ìåííèê³â
print q
poly=q/len(set(ns))
print '\nñåğåäíº çíà÷åííÿ ïîë³ñåì³¿'
print round(poly,3)
     
print '\n>> task 14 <<'
#from nltk.probability import *
a=[('car','automobile'),('gem','jewel'),('journey','voyage'),('boy','lad'),
   ('coast','shore'),('asylum','madhouse'),('magician','wizard'),('midday','noon'),
   ('furnace','stove'),('food','fruit'),('bird','cock')]
s=[]
w1=[]
w2=[]
for i,j in a: #öèêë ïî ñëîâàì ç êîğòåæ³â ó ñïèñêó à
    aa=wn.synsets(i)#ñïèñîê ñèíñåò³â ïåğøîãî ñëîâà
    bb=wn.synsets(j)#ñïèñîê ñèíñåò³â äğóãîãî ñëîâà
    for a1 in aa: #öèêë ïî ñèíñåòàõ ïåğøîãî ñëîâà
  #  s.append('Znachenya podibnosti dlya:') #â ğåçóëüòóş÷èé ñïèñîê òåêñò
        w1.append(a1) #â ğåçóëüòóş÷èé ñïèñîê ñèíñåò 
    for b1 in bb: #öèêë ïî ñèíñåòàõ äğóãîãî ñëîâà
   # s.append('ta:') #â ğåçóëüòóş÷èé ñïèñîê òåêñò
        w2.append(b1) #â ğåçóëüòóş÷èé ñïèñîê ñèíñåò
    res=a1.path_similarity(b1) #â ğåçóëüòóş÷èé ñïèñîê çíà÷åííÿ ïîä³áíîñò³ ì³æ ñèíñåòàìè
print '\n Ïîñîğòîâàíèé ñïèñîê 1 \n'
print w1
print '\n Ïîñîğòîâàíèé ñïèñîê 2 \n'
print w2
print '\n Ñåìàíòè÷íà ïîä³áí³ñòü \n'
print res
     
