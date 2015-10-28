from __future__ import division
import nltk, re, pprint
import urllib, nltk
from urllib import urlopen

#Task1
#�������� �������, ��� ������ ������ URL, �� ��������, � ������� �� �� �������� �� ���� ������� � ���������� HTML �������.
#��������������� urllib.urlopen ��� ������� �� �������� ��������� ����� raw_contents = urllib.urlopen('http://www.nltk.org/').read().
print "\n1)"

url = "http://www.nltk.org/"
raw = urlopen(url).read()
raw_contents = nltk.clean_html(data)
tokens = nltk.word_tokenize(raw_contents)
print tokens[:30]

#Task2
#�������� ������ ����� � ���� corpus.txt. ��������� ������� load(f) ��� ������� �����, ����� ����� � �� ���������� � ������� ������, ��� ������ ����� � �����.
print "\n2)"

def load(f):
	a=open(f)
	raw = a.read()
	return raw
print

#Task3
#���������� ��������� ���� �� list comprehension:
print "\n3)"
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = []
for word in sent:
    word_len = (word, len(word))
    result.append(word_len)

print result

result1 = [(word, len (word)) for word in sent]
print result1

#Task4
#��������� ������ �� �������� � ����� ��������� ������� 䳿: "3" * 7 �� 3 * 7.
#��������� �������� ������������� �� �������� � ������ ������������ int("3") �� str(3).
print "\n4)\n"
print '3' * 7
print 3 * 7
print int("3") * 7
print str(3) * 7

#Task5
#�� ���������, ���� ������ ������������ %6s �� %-6s
#��������������� ��� ����������� ������ ����� �� 6 �������?
print "\n5)\n"
print '%6s' % 'dogdogdog'
print '%6s' % 'dog'
print '%-6s' % 'dogdogdogdog'
print '%-6s' % 'dog' 

#Task7
#������� ����, ���� ���� ������ ����� �� �� ������� ������� � �������
#������ ����� ����� ( fuzzy 53).
#���������� ��� ���� �������������� open(filename).readlines().
#������� ����� ������ �� �� ������� �������������� split(),
#� ���������� ����� � ���� �������� �������������� int().
#��������� ������� ���� � ������ ������: [['fuzzy', 53], ...].
print "\n7)\n"
myfile = "path/lab5_words.txt"

myList = []

f = open(myfile).readlines()
for line in f:
    word = line.split()[0]
    intVariable = int(line.split()[1])
    lineList = [word, intVariable]
    myList.append(lineList)    
print myList

#Task8
#�������� �������� ������� �� ���������� � ��������� � �� ������� ������.
print "\n8)\n"
url = "http://www.bbc.com/travel/story/20151019-the-macau-secret-to-living-a-long-life"
html = urlopen (url).read ()
raw = nltk.clean_html (html)
tokens = nltk.word_tokenize (raw)
tokens [100:150]

#Task10
#������ random ������ ������� choice(), ��� ���������� ����� ������ �������� �����������.
#���������, choice("aehh ") ���� �������� ���� � �������� �������.
#�������� �������� ��������� ������ � 500 ��������� �������� ������� "aehh ".
#��� �������� �������� � ������ �������������� ''.join() .
#����������� ��������� ��������� �������������� split() �� join().
import random
line = []
sym = 'aehh'
for element in range (500):
    line.append (random.choice (sym))

line2 = ' '.join (line)
print line2
print line2.split ()

#Task15
#���������� ��������� ����, �� list comprehension:
print "\n15)\n"
words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = set()
for word in words:
    vowels = []
    for char in word:
        if char in 'aeiou':
            vowels.append(char)
            vsequences.add(''.join(vowels))
print vsequences
print sorted(vsequences)

print ">>>>>\t\t\ 2nd method>>>>\t"
[vsequences.add(''.join(vowels)) for vowels in [char for char in word if char in 'aeiou']]
print sorted (vsequences)

