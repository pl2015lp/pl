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

# ����� �� �������� � wn
ns=[]

for i in wn.all_synsets('n'):
    for j in i.lemma_names:
        ns.append(j) #� ������ ����� �� ����� ��� (�� �������� ��� � ���������)
num=len(set(ns))#������� �������� � WN
print num
q=0
for i in set(ns):  # ��������� �� ��������
    q=q+len(wn.synsets(i,'n'))  # ����� �������� ��������
print q
poly=q/len(set(ns))
print '\n������ �������� �����쳿'
print round(poly,3)
     
print '\n>> task 14 <<'
#from nltk.probability import *
a=[('car','automobile'),('gem','jewel'),('journey','voyage'),('boy','lad'),
   ('coast','shore'),('asylum','madhouse'),('magician','wizard'),('midday','noon'),
   ('furnace','stove'),('food','fruit'),('bird','cock')]
s=[]
w1=[]
w2=[]
for i,j in a: #���� �� ������ � ������� � ������ �
    aa=wn.synsets(i)#������ ������� ������� �����
    bb=wn.synsets(j)#������ ������� ������� �����
    for a1 in aa: #���� �� �������� ������� �����
  #  s.append('Znachenya podibnosti dlya:') #� ������������ ������ �����
        w1.append(a1) #� ������������ ������ ������ 
    for b1 in bb: #���� �� �������� ������� �����
   # s.append('ta:') #� ������������ ������ �����
        w2.append(b1) #� ������������ ������ ������
    res=a1.path_similarity(b1) #� ������������ ������ �������� �������� �� ���������
print '\n ������������ ������ 1 \n'
print w1
print '\n ������������ ������ 2 \n'
print w2
print '\n ���������� �������� \n'
print res
     
