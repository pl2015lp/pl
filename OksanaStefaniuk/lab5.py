# -*- coding: utf8 -*-
from __future__ import division
import nltk, re, pprint
import urllib, nltk
from urllib import urlopen

#Task1
#Íàïèø³òü ôóíêö³þ, ÿêà ïðèéìàº àäðåñó URL, ÿê àðãóìåíò, ³ ïîâåðòàº òå ùî ì³ñòèòüñÿ çà ö³ºþ àäðåñîþ ç âèäàëåííÿì HTML ðîçì³òêè.
#Âèêîðèñòîâóâàòè urllib.urlopen äëÿ äîñòóïó äî êîíòåíòó íàñòóïíèì ÷èíîì raw_contents = urllib.urlopen('http://www.nltk.org/').read().
print "\n1)"

url = "http://www.nltk.org/"
raw = urlopen(url).read()
raw_contents = nltk.clean_html(data)
tokens = nltk.word_tokenize(raw_contents)
print tokens[:30]

#Task2
#Çáåðåæ³òü äåÿêèé òåêñò ó ôàéë³ corpus.txt. Âèçíà÷èòè ôóíêö³þ load(f) äëÿ ÷èòàííÿ ôàéëó, íàçâà ÿêîãî º ¿¿ àðãóìåíòîì ³ ïîâåðòàº ñòð³÷êó, ÿêà ì³ñòèòü òåêñò ç ôàéëó.
print "\n2)"

def load(f):
	a=open(f)
	raw = a.read()
	return raw
print

#Task3
#Ïåðåïèø³òü íàñòóïíèé öèêë ÿê list comprehension:
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
#Ïåðåâ³ðèòè ð³çíèöþ ì³æ ñòð³÷êàìè ³ ö³ëèì âèêîíàâøè íàñòóïí³ ä³¿: "3" * 7 òà 3 * 7.
#Ñïðîáóéòå çä³éñíèòè êîíâåðòóâàííÿ ì³æ ñòð³÷êàìè ³ ö³ëèìè âèêîðèñòàâøè int("3") òà str(3).
print "\n4)\n"
print '3' * 7
print 3 * 7
print int("3") * 7
print str(3) * 7

#Task5
#Ùî ñòàíåòüñÿ, êîëè ñòð³÷êè ôîðìàòóâàííÿ %6s òà %-6s
#âèêîðèñòîâóºòüñÿ äëÿ â³äîáðàæåííÿ ñòð³÷êè äîâøî¿ í³æ 6 ñèìâîë³â?
print "\n5)\n"
print '%6s' % 'dogdogdog'
print '%6s' % 'dog'
print '%-6s' % 'dogdogdogdog'
print '%-6s' % 'dog' 

#Task7
#Ñòâîð³òü ôàéë, ÿêèé áóäå ì³ñòèòè ñëîâà òà ¿õ ÷àñòîòó çàïèñàí³ â îêðåìèõ
#ðÿäêàõ ÷åðåç ïðîá³ë ( fuzzy 53).
#Ïðî÷èòàéòå öåé ôàéë âèêîðèñòîâóþ÷è open(filename).readlines().
#Ðîçä³ë³òü êîæíó ñòð³÷êó íà äâ³ ÷àñòèíè âèêîðèñòîâóþ÷è split(),
#³ ïåðåòâîð³òü ÷èñëî â ö³ëå çíà÷åííÿ âèêîðèñòîâóþ÷è int().
#Ðåçóëüòàò ïîâèíåí áóòè ó âèãëÿä³ ñïèñêó: [['fuzzy', 53], ...].
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
#Íàïèø³òü ïðîãðàìó äîñòóïó äî âåáñòîð³íêè ³ âèëó÷åííÿ ç íå¿ äåÿêîãî òåêñòó.
print "\n8)\n"
url = "http://www.bbc.com/travel/story/20151019-the-macau-secret-to-living-a-long-life"
html = urlopen (url).read ()
raw = nltk.clean_html (html)
tokens = nltk.word_tokenize (raw)
tokens [100:150]

#Task10
#Ìîäóëü random âêëþ÷àº ôóíêö³þ choice(), ÿêà âèïàäêîâèì ÷èíîì âèáèðàº åëåìåíòè ïîñë³äîâíîñò³.
#Íàïðèêëàä, choice("aehh ") áóäå âèáèðàòè îäèí ç ÷îòèðüîõ ñèìâîë³â.
#Íàïèø³òü ïðîãðàìó ãåíåðàö³¿ ñòð³÷êè ç 500 âèïàäêîâî âèáðàíèõ ñèìâîë³â "aehh ".
#Äëÿ ïîºäíàííÿ åëåìåíò³â â ñòð³÷êó âèêîðèñòîâóéòå ''.join() .
#Íîðìàë³çóéòå îòðèìàíèé ðåçóëüòàò âèêîðèñòîâóþ÷è split() òà join().
import random
line = []
sym = 'aehh'
for element in range (500):
    line.append (random.choice (sym))

line2 = ' '.join (line)
print line2
print line2.split ()

#Task15
#Ïåðåïèø³òü íàñòóïíèé öèêë, ÿê list comprehension:
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

