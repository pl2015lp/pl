print '========= Task 1 ========='
sent1=['I','love','to','listen','to','music']
print sent1
sent2=sent1
print sent2
sent1[3]='why'
print 'sent1=', sent1
print 'sent2=', sent2

print '========= Task 4 ========='

import copy
from copy import deepcopy

test_1 = [1, 2, 3, [1, 2, 3]]
test_copy = copy.copy(test_1)
print(test_1, test_copy)

test_copy[3].append(4)
print(test_1, test_copy)

test_1 = [1, 2, 3, [1, 2, 3]]
test_deepcopy = copy.deepcopy(test_1)
test_deepcopy[3].append(4)
print(test_1, test_deepcopy)
print '==========================================='
r = [1, 2, 3]
r.append(r)
print(r)

p = copy.deepcopy(r)
print(p)


print '========= Task 9 ========='
letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,'i':10, 'j':10,
             'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200,'s':300,
            't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
def gematria(word):
    sum=0
    for letter in word:
        sum+=letter_vals[letter]
    return sum
print '=============================================='	    
print gematria('mother')


print '========= Task 12 ========='
text1='A new study shows that college students need to be doing a lot more to set themselves up for a job after college. According to the report, conducted by career website AfterCollege from a March survey of 600 college students, 79%of students have done at least one internship in the past six months, but 57% of those internships were unpaid and 76% did not result in a job offer.'

text1='Swediosed a threat to public order.The controls will come into effect from midday local time on Thursday and will last initially for 10 days.EU and African leaders are to hold a second day of talks in Malta to discuss measures to stem the flow of migrants.'
import nltk
def shorten(text,n):
	fd=nltk.FreqDist(nltk.word_tokenize(text))
	b=fd.keys()[:n]
	c=[]
	for i in nltk.word_tokenize(text):
		if i not in b:
			c+=[i]
	import string
	print'the most frequent words:' ,b
	return string.join(c)
print shorten(text1,10)


print '========= Task 15 ========='
a=['key','good','disgust','love','excellent','student','prom']
dict=['key','good','student']
def diff(text,dic):
    return set(text).difference(dic)

print diff(a,dict)

print '========= Task 17 ========='

import nltk

print nltk.edit_distance('curry','criminal')

print nltk.edit_distance('bartender','breathe')

print nltk.edit_distance('cool','cold')






