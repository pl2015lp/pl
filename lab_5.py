from __future__ import division
import nltk, re, pprint


import urllib, nltk
from urllib import urlopen

print '========= Task 1 ========='
#1. �������� �������, ��� ������ ������ URL, �� ��������, � ������� �� �� �������� �� ���� ������� � ���������� HTML �������.
#��������������� urllib.urlopen ��� ������� �� �������� ��������� ����� raw_contents = urllib.urlopen('http://www.nltk.org/').read().

link = "http://www.nltk.org/"
data = urlopen(link).read()
raw = nltk.clean_html(data)
t = nltk.word_tokenize(raw)
print 'Text of loaded and parssed url: \n', t[:30]

print '\n ========= Task 2 ========='
#2.�������� ������ ����� � ���� corpus.txt. ��������� ������� load(f) ��� ������� �����, ����� ����� � �� ����������
# � ������� ������, ��� ������ ����� � �����.
path  = 'C:\py'
f = open(path+'\corpus.txt','w')
for w in t:
    f.write(w+' ')
f.close()
newf = open(path+'\corpus.txt', 'r')
data = newf.read()
print 'String from file corpus.txt: \n', data[:187], '...'

print '\n ========= Task 3 ========='
#���������� ��������� ���� �� list comprehension:
sent = ['The', 'dog', 'gave', 'John', 'the','newspaper']
result=[(word, len(word)) for word in sent]
print result


print '\n ========= Task 4 ========='
#4. ��������� ������ �� �������� � ����� ��������� ������� 䳿: "3" * 7 �� 3 * 7.
#��������� �������� ������������� �� �������� � ������ ������������ int("3") �� str(3).

a="3"
print 'The first case: "3" * 7 =', a*7
print 'The second case: 3 * 7 =', 3*7
print 'Conversation int("3") =', int("3")
print 'Conversation str(3) =' , str(3)

print '\n ========= Task 5 ========='
#5.	�� ���������, ���� ������ ������������ %6s �� %-6s ��������������� ��� ����������� ������ ����� �� 6 �������?
print '6 spaces before:','%6s' % 'str'
print '6 spaces after:','%-6s' % 'str'

#���� ������� ������ �� ����� 6 �������, �� ������� ������ ��������� �������� �� ������� 6 ������� � �������� ����� �������� �� ������� ���� (%6s)
#��� �� ����� ����(%-6s).
#���� � �� ������������� %6s ��� %-6s �� ������ ����� �� 6 �������, �� � ������� ����� �� ����������.

print '\n ========= Task 7 ========='
#7. ������� ����, ���� ���� ������ ����� �� �� ������� ������� � ������� ������ ����� ����� ( fuzzy 53). ���������� ��� ���� ��������������
# open(filename).readlines().  ������� ����� ������ �� �� ������� �������������� split(),� ���������� ����� � ���� �������� �������������� int().
#��������� ������� ���� � ������ ������: [['fuzzy', 53], ...].

file = open('E:\doc.txt')
p=file.readlines()
print p
a=[]
for i in p:
    c=i.split()
    a.append([i.split()[0],int(i.split()[1])])

print '\n ========= Task 10 ========='
# ������ random ������ ������� choice(), ��� ���������� ����� ������ �������� �����������. ���������, choice("aehh ") ���� �������� ���� � �������� �������.
#�������� �������� ��������� ������ � 500 ��������� �������� ������� "aehh ".
#��� �������� �������� � ������ �������������� ''.join() . ����������� ��������� ��������� �������������� split() �� join().
import random
aa=''
for i in range(500):
    aa=aa+''.join(random.choice("aehh "))
print  aa[:50]
bb=aa.split()
print bb[:15]


print '\n ========= Task 13 ========='
13.	�������������� Porter ������ ����������� ����-���� ������������ ����� . �� ���� ������ ������ ���������� Lancaster ������.
���������� ��������� �� �������.

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

print '\n ========= Task 14 ========='
#14.	���������� �� ������ ABC Rural News �� ABC Science News � ������� (nltk.corpus.abc).
#������� �������� ��� ������ ������������ ������ (��������� �� ������ �12).
#�������������� Punkt ��� ����� ������ �� ����� �������.

from nltk.corpus import abc
l=0
n=0
for w in nltk.corpus.abc.words():
    l+=len(w)
    n+=1
    mw = l/n #������� �-��� ���� � ����
print mw
ms = len(nltk.corpus.abc.words()) / len(nltk.corpus.abc.sents())#������ �������� �-�� ��� � ������ � ����� 
print ms
ari = 4.71*mw+0.5*ms-21.43# �������� ��� ������ ������������ �� ��� �������
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
'''
#Task 2

def load(f):
    a=open('E:\corpus.txt', 'r')
    data = a.read()
    for line in data:
        k=line.strip()
    return k








