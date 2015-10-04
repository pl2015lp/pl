# -*- coding: cp1251 -*-
import nltk
from nltk.book import *
#Task2
#Створіть змінну sentence і присвойте їй значення ‘she sells sea shells by the sea shore'
#Напишіть фрагмент програми для виведення на екран всіх сліва, довжина яких більша ніж 4 символи.
print "\n1)"
sentence='she sells sea shells by the sea shore'
list1=sentence.split()
print list1
for word in list1:
    if len(word)>4:
        print word
#Task6
#Перегляньте результати виконання умовних виразів: ’row’ in ’brown’ та ’row’ in [’ brown’, ’cow’].
#Напишіть програму для перевірки наявності в стрічці sent=’ ’colorless green ideas sleep furiously’ окремих слів та підстрічок.
print "\n2)"
one = 'row' in 'brown'
two= 'row' in ['brown', 'cow']
print "'row' in 'brown' - " + str(one)
print "'row' in ['brown', 'cow'] - " + str(two)
sent='colorless green ideas sleep furiously'
words=sent.split()
subword='furious'
for oneword in words:
    if oneword.startswith(subword):
        print "subword '%s' was found in word '%s'" % (subword, oneword)
#Task8
#Виконати наступні приклади і пояснити різницю між ними:w.isupper() not w.islower()
print "\n3)"
str2='colorless GREEN ideas Sleep furiosly'
words2=str2.split()
for word in words2:
    print "'%s' is Upper? - [%s]" % (word, word.isupper())
    print "'%s' is Lower? - [%s]" % (word, word.islower())
#Task13
#Перевірте виконання виразу set(sent3) < set(text1).
#Змініть аргументи функції. Результати поясніть.
print "\n4)"
a = set(sent3) < set(text2)
print "%s < %s - %s" % (sent3, text2, a)

#Task12
#Використайте вираз sum([len(w) for w in text1]) для знаходження середньої довжини слів в тексті.
print "\n5)"
numberofchars=sum([len(w) for w in text1])
numberofwords=len(text1)
average=numberofchars/numberofwords
print average
#Task16
#Побудуйте колокації для текстів №1 та №5. Результати порівняйте.
print "\n6)"
print '\n text1 \n'
text1.collocations()
print '\n text5 \n'
text5.collocations()
if text1.collocations() == text5.collocations():
    print ('collocations are equal')
else:
    print ('collocations are unequal')
