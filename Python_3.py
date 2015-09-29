#3.1. �������������� ������ corpus ���������� ����� austin-persuasion.txt. ��������� ������ tokens (���) � type (��������� ���)������ �� ������.
import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
austen = gutenberg.words('austen-persuasion.txt')
print len(austen)
fdist = FreqDist(austen)
vocabulary = fdist.keys()
print vocabulary

#3.5. ������� ���� ������ � ������� �������� �� ���� (������� ����������� ���, ��������� ����, ����). ������� �����, �� ����� ����� ���� � ��� �������, ������ �� ����� monstrous � Moby Dick �� � Sense and Sensibility. 
import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
n1 = brown.words(fileids=['ck11'])
n2 = brown.words(fileids=['cf16'])
list1 = []
list2 = []
print '==============original words=================='
fdist1 = FreqDist(n1)
voc1 = fdist1.keys()
print len(voc1)
fdist2 = FreqDist(n2)
voc2 = fdist2.keys()
print len(voc2)
print '============words with 1 apperence============'
for w in n1:
    if w.isalpha() and fdist1[w] == 1:
        list1.append(w)
print len(list1)
for w in n2:
    if w.isalpha() and fdist2[w] == 1:
        list2.append(w)
print len(list2)
print '==================genres======================'
print brown.categories(['ck11'])
print brown.categories(['cf16'])

#3.7. �������� �������� ��� ����������� ��� ��� � ������ Brown, �� ������������ �� ���� �� ��� ����.	
import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
text = brown.words()
fdist = nltk.FreqDist([w.lower() for w in text])
for i in text:
    if fdist[i] >= 3:
        print i
 
#3.8. �������� �������� ��������� ������� ��������  ������� ���/������� ����������� ��� ��� ��� ����� ������� Brown. ������������ ������� ���������� �� ������� ��.
import nltk
from nltk.probability import FreqDist
from nltk.corpus import brown
j=0
genres = [u'adventure', u'belles_lettres', u'editorial', u'fiction', u'government', u'hobbies', u'humor', u'learned', u'lore', u'mystery', u'news', u'religion', u'reviews', u'romance', u'science_fiction']
for i in genres:
    abc = brown.words(categories=i)
    fr = FreqDist(brown.words(categories=i))
    key = fr.keys()
    kil = len(abc)/len(key)
    print genres[j], kil
    j+=1

#3.9. �������� �������� ��� ����������� 50 ������������� ��� � �����, �� ����������� ���������� ���.
import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
austen = gutenberg.words('austen-persuasion.txt')
fdist = FreqDist(austen)
p = [w for w in fdist if w.isalpha()]
print p[:50]

#3.12. �������� ������� word_freq(), ��� ������ ����� � ����� ������� ������� Brown �� ��������� � ������� ������� ����� � ������ ������ �������.
import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
def word_freq(word, name):
    n = brown.words(fileids=[name])
    fdist = FreqDist(n)
    print fdist[word]
word_freq('in', 'cf15')
