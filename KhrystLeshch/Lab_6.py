# -*- coding: utf-8 -*-
from __future__ import division
import nltk, re, pprint
print "task1"
# Описати, які класи стрічок відповідають наступному регулярному виразу. [a-zA-Z]+. Результати перевірити використовуючи nltk.re_show()
f=open('C://Python27/KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('[a-zA-Z]+', raw)


print "task2"
# Описати, які класи стрічок відповідають наступному регулярному виразу. [A-Z][a-z]*. Результати перевірити використовуючи nltk.re_show()
f=open('C://Python27/KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('[A-Z][a-z]*', raw)

print "task3"
# Описати, які класи стрічок відповідають наступному регулярному виразу. \d+(\.\d+)?. Результати перевірити використовуючи nltk.re_show()
f=open('C://Python27/KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('\d+(\.\d+)?', raw)

print "task4"
# Описати, які класи стрічок відповідають наступному регулярному виразу. ([^aeiou][aeiou][^aeiou])*. Результати перевірити використовуючи nltk.re_show()
f=open('C://Python27/KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('([^aeiou][aeiou][^aeiou])*', raw)


print "task5"
# Описати, які класи стрічок відповідають наступному регулярному виразу. \w+|[^\w\s]+.. . Результати перевірити використовуючи nltk.re_show()
f=open('C://Python27/KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('\w+|[^\w\s]+.', raw)


print "task6"
# Описати, які класи стрічок відповідають наступному регулярному виразу. p[aeiou]{,2}t . Результати перевірити використовуючи nltk.re_show()
f=open('C://Python27/KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('p[aeiou]{,2}t', raw)


print "task7"
# Написати регулярний вираз, який встановлює відповідність наступному класу стрічок: всі артиклі ( a, an, the)
import re
pattern = r"[a-z]+"
word_re = re.compile(pattern)
print word_re.findall("a an the")


print "task12"
# Написати регулярний вираз для токенізації такого тексту, як don't до do та n't? Пояснити чому цей регулярний вираз не працює: "n't| \w+"
a = "don't"
print nltk.re_show ("n't|\w+", a)
print nltk.re_show ("do|n't", a)




print "task14"
# Прочитати файл допомоги про функцію re.sub() використовуючи help(re.sub). Використовуючи re.sub  напишіть програму видалення HTML розмітки замінивши її на пробіли.
print help(re.sub)
url="http://www.bbc.com/news/world-europe-34595409"
html=urlopen(url).read()
print html [:300] 
a = html[:300]
print a 
print re.sub(r"<.*>",'',a) 


print "task15"
# Прочитати Додаток А. Дослідити явища описані у Додатку А використовуючи корпуси текстів та метод findall() для пошуку в токенізованому тексті.
import nltk
from nltk.corpus import gutenberg, nps_chat, brown
moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
print moby.findall(r"<the> <best> (<.*>) <can>") 
chat=nltk.Text (nps_chat.words())
print chat.findall(r"<the> <best> (<.*>) <can>")
brown1=nltk.corpus.brown(categories='adventure')
print brown1.findall (r"<the> <best>(<.*>) <can>") 

