# -*- coding: utf-8 -*-

#Task1
#Описати, які класи стрічок відповідають наступному регулярному виразу. [a-zA-Z]+. Результати перевірити використовуючи nltk.re_show()

from_future_import division
import nltk, re, pprint

print "\n1)\n"

f=open('D://KL/Lab6/text.txt')
raw=f.read()
print nltk.re_show ('[a-zA-Z]+', raw)

#Task2
#Описати, які класи стрічок відповідають наступному регулярному виразу. [A-Z][a-z]*.
#Результати перевірити використовуючи nltk.re_show()

print "\n2)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('[A-Z][a-z]*', raw)

#Task3
#Описати, які класи стрічок відповідають наступному регулярному виразу. \d+(\.\d+)?.
#Результати перевірити використовуючи nltk.re_show()

print "\n3)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('\d+(\.\d+)?', raw)

#Task4
#Описати, які класи стрічок відповідають наступному регулярному виразу. ([^aeiou][aeiou][^aeiou])*.
#Результати перевірити використовуючи nltk.re_show()

print "\n4)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('([^aeiou][aeiou][^aeiou])+', raw)

#Task5
#Описати, які класи стрічок відповідають наступному регулярному виразу. \w+|[^\w\s]+..
#Результати перевірити використовуючи nltk.re_show()

print "\n5)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('\w+|[^\w\s]+.', raw)

#Task6
#Описати, які класи стрічок відповідають наступному регулярному виразу. p[aeiou]{,2}t
#Результати перевірити використовуючи nltk.re_show()

print "\n6)\n"

f = open ('path/textForlab5.txt')
raw = f.read ()
nltk.re_show ('p[aeiou]{,2}t', raw)

#Task7
#Написати регулярний вираз, який встановлює відповідністьнаступному класу стрічок:
#арифметичний вираз з цілими значеннями і, який містить операції множення та додавання (2*3+8).

print "\n8)\n"

l='2*3+8'
nltk.re_show (r"\d+[+|*]\d+[+|*]\d+", l)
{2*3+8}

#Task8
#Зберегти довільний текст у файлі corpus.txt. Визначити функцію  для читання з цього файлу (назва файлу аргумент функції) і повертає стрічку, яка містить текст з файлу.
#Використовуючи nltk.regexp_tokenize() розробити токенізатор для токенізації різних типів виразів: грошові одиниці, дати, імена людей та організацій.
#Використовувати багаторядковий запис регулярного виразу з коментарями та «verbose flag».

print "\n10)\n"

f=open('C:\Python27\corpus2.txt')
text=f.read()
pattern=r'''(?x)
\$\d+(\.\d+)?       
| (\d{,2}\.\d{,2}\.\d{4})|\d{4}
| ([A-Z]\w+([\ -])?){2,}
| [A-Z]{2,}
'''
print nltk.regexp_tokenize(text, pattern)

#Task9
#Напишіть програму, яка конвертує текст в Pig Latin. String->ingstray, idle->idleay.
#(Конвертація відбувається переміщенням приголосної або групи приголосних на початок слова та додаванням до слова ay ).

print "\n13)\n"

import nltk, re
from nltk.corpus import gutenberg
def latin(w):
    piece-re.findall(regexp, w)
    pos=len(piece[0])
    new=w[pos:] + piece[0] + 'ay'
    return new
raw=gutenberg.raw('austen-sense.txt')
text=re.split(r'[\W\d]+', raw)
print text [:20]
regexp =r'^[^AEIOUaeiou]*'
pig_latin=[]
for word in text:
    pig_latin.append(latin(word))
    print pig_latin[:20]

#Task10
#Прочитати Додаток А.
#Дослідити явища описані у Додатку А використовуючи корпуси текстів та метод findall()для пошуку в токенізованому тексті. 

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
