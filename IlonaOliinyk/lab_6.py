# -*- coding: utf-8 -*-
#1. Описати, які класи стрічок відповідають наступному регулярному виразу.
#[a-zA-Z]+.
#Результати перевірити використовуючи nltk.re_show( ).

from __future__ import division
import nltk, re, pprint

print "\n1)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('[a-zA-Z]+', raw)
# Виділяє слова, які містять одну або більше букв великого чи малого регістру


#2.	Описати, які класи стрічок відповідають наступному регулярному виразу.
#[A-Z][a-z]*.
#Результати перевірити використовуючи nltk.re_show()

print "\n2)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('[A-Z][a-z]*', raw)

#Виділяє слова, які мають у своєму складі одну велику букву
#і можуть мати маленькі літери


#3.  Описати, які класи стрічок відповідають наступному регулярному виразу.
#\d+(\.\d+)?.
#Результати перевірити використовуючи nltk.re_show()

print "\n3)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('\d+(\.\d+)?', raw)

#\d+  [0-9]+ цифра має бути хоча б один раз або більше разів 
#\.   крапка
# ? pattern повторюється 1 або жодного разу

# 4.	Описати, які класи стрічок відповідають наступному регулярному виразу.
#([^aeiou][aeiou][^aeiou])*. Результати перевірити використовуючи nltk.re_show() 
print "\n4)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('([^aeiou][aeiou][^aeiou])+', raw)

#[^aeiou] - перший символ - не голосна літера
#[aeiou] - наступний символ - голосна
#[^aeiou] - наступний знову не голосна
#+ - повторяюється хоча б 1 раз


#5.	Описати, які класи стрічок відповідають наступному регулярному виразу.
#\w+|[^\w\s]+..
#Результати перевірити використовуючи nltk.re_show()
print "\n5)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('\w+|[^\w\s]+.', raw)


#будь-яка буква або цифра 1 або більше раз, або (не буква і не цифра) і не пропуском 1 або быільше раз
#\w+  - будь який символ (цифра або буква)
#|   -  або
##[^\w\s]+  - НЕ символ(-+*) і НЕ пропуск

#6.	Описати, які класи стрічок відповідають наступному регулярному виразу.
#p[aeiou]{,2}t  Результати перевірити використовуючи nltk.re_show()

print "\n6)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('p[aeiou]{,2}t', raw)

#p, 0-2 голосні, t

#7.	Написати регулярний вираз, який встановлює відповідність
#наступному класу стрічок: всі артиклі (a, an, the).
print "\n7)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('an|a|the', raw)




#12.	Написати регулярний вираз для токенізації такого тексту,
#як don't до  do та n't?
#Пояснити  чому цей регулярний вираз не працює: «n't|\w+».
print "\n12)\n"
b = "don't"

nltk.re_show("do|n't", b)


#14.	Прочитати файл допомоги  про функцію re.sub() використовуючи
#help(re.sub) . Використовуючиre.sub напишіть програму видалення
#HTML розмітки замінивши її на пробіли.
print "\n14)\n"
import urllib, nltk, re
from urllib import urlopen
help(re.sub)
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read()
a = html[0:400]
print re.sub(r"<.*>",' ',a)

#15.	Прочитати Додаток А. Дослідити явища описані у Додатку А використовуючи
#корпуси текстів та метод findall()для пошуку в токенізованому тексті.
print "\n15)\n"

import nltk
from nltk.corpus import gutenberg, brown
print 'Gutenberg:\n'
text1 = nltk.Text(gutenberg.words('edgeworth-parents.txt'))
print text1.findall(r'<the> <best> (<\w*>) <can>')
print text1.findall(r'<as> <best> (<\w*>) <can>')
print text1.findall(r'<as> <best> <as>(<\w*>) <can>')
print text1.findall(r'<the> <best> <that>(<\w*>) <can>')
print '\nBrown:\n'
text2 = nltk.Text(brown.words(categories='adventure'))

print text2.findall(r'<the> <best> (<\w*>) <can>')
print text2.findall(r'<as> <best> (<\w*>) <can>')
print text2.findall(r'<as> <best> <as>(<\w*>) <can>')
print text2.findall(r'<the> <best> <that>(<\w*>) <can>')






