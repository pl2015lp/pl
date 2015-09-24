# -*- coding: cp1251 -*-
import nltk
from nltk.book import *
#1)
#Створіть змінну sentence і присвойте їй значення
#‘she sells sea shells by the sea shore’
#та напишіть фрагмент програми, яка генерує нову стрічку
#додаючи ‘like’ перед кожним зі слів , яке починається з ‘se’.
print "\n1)>>>>3\n"

str1 = 'she sells sea shells by the sea shore'
words = str1.split()
newString = ""

for oneWord in words:
    if oneWord.startswith('se'):
        newString += "like " + oneWord + " "
    else: newString += oneWord + " "

print newString

#2)
#Перегляньте результати виконання умовних виразів:
#’row’ in ’brown’ та ’row’ in [’ brown’, ’cow’].
#=============
#Напишіть програму для перевірки наявності в стрічці
# sent=’ ’colorless green ideas sleep furiously’ окремих слів та підстрічок.
print "\n2)>>>>6\n"

a = 'row' in 'brown'
b = 'row' in ['brown', 'cow']
c = 'row' in ['brown', 'row']
print "'row' in 'brown' - " + str(a)
print "'row' in ['brown', 'cow'] - " + str(b)
print "'row' in ['brown', 'row'] - " + str(c)

sent = 'colorless green ideas sleep furiously'
words = sent.split()
subWord = 'Color'

for oneWord in words:
    if oneWord.lower().startswith(subWord.lower()):
        print "subword '%s' was found in word '%s'" % (subWord, oneWord)



#3)
#Виконати наступні приклади і пояснити різницю між ними
#w.isupper() 
#not w.islower()
print "\n>>>>8\n"

str3 = 'She sells sea SHELLS By THE sea shore'
words3 = str3.split()
for word in words3:
    #All the letters in word are upper
    print "'%s' is Upper? - [%s]" % (word, word.isupper())
    #All the letters in word are lower
    print "'%s' is Lower? - [%s]" % (word, word.islower())
    #The first letter of the word is title
    print "'%s' is Title? - [%s]" % (word, word.istitle())
    
#4
#Перевірте виконання виразу set(sent3) < set(text1).
#Змініть аргументи функції. Результати поясніть.
print "\n)>>>>13\n"
# Is the length of sentence3 smaller than the length of text3?
a = set(sent3) < set(text2)
print "IS SENTENCE_3: %s < than TEXT_2: %s - %s"  % (sent3, text2, a)
# Is the length of sentence3 smaller than the length of text3?
b = set(sent3) > set(text2)
print "IS SENTENCE_3: %s > than TEXT_2: %s - %s"  % (sent3, text2, b)
#5
#Використайте вираз sum([len(w) for w in text1])
#для знаходження середньої довжини слів в тексті.
print "\n5)>>>>12\n"
numberOfChars = sum([len(w) for w in text1])
numberOfWords = len(text1)
avarageLength =  float(numberOfChars)/(numberOfWords)
print "Number of chars in the text is %s" % (numberOfChars)
print "Number of words in the text is %s" % (numberOfWords)
print "Avarage length of words is - %s" % (avarageLength)

#6
#Побудувати колокації текстів 1 та 2. Порівняйте результати.

print "\n5)>>>>14\n"
print '\n text1 \n'
text1.collocations()
print '\n text2 \n'
text2.collocations()
if text1.collocations() == text2.collocations():
    print ('collocations are equal')
else:
    print ('collocations are unequal')




