from __future__ import division
import nltk, re, pprint


import urllib, nltk
from urllib import urlopen

print '========= Task 1 ========='
#1. Напишіть функцію, яка приймає адресу URL, як аргумент, і повертає те що міститься за цією адресою з видаленням HTML розмітки.
#Використовувати urllib.urlopen для доступу до контенту наступним чином raw_contents = urllib.urlopen('http://www.nltk.org/').read().

link = "http://www.nltk.org/"
data = urlopen(link).read()
raw = nltk.clean_html(data)
t = nltk.word_tokenize(raw)
print 'Text of loaded and parssed url: \n', t[:30]

print '\n ========= Task 2 ========='
#2.Збережіть деякий текст у файлі corpus.txt. Визначити функцію load(f) для читання файлу, назва якого є її аргументом
# і повертає стрічку, яка містить текст з файлу.
path  = 'C:\py'
f = open(path+'\corpus.txt','w')
for w in t:
    f.write(w+' ')
f.close()
newf = open(path+'\corpus.txt', 'r')
data = newf.read()
print 'String from file corpus.txt: \n', data[:187], '...'

print '\n ========= Task 3 ========='
#Перепишіть наступний цикл як list comprehension:
sent = ['The', 'dog', 'gave', 'John', 'the','newspaper']
result=[(word, len(word)) for word in sent]
print result


print '\n ========= Task 4 ========='
#4. Перевірити різницю між стрічками і цілим виконавши наступні дії: "3" * 7 та 3 * 7.
#Спробуйте здійснити конвертування між стрічками і цілими використавши int("3") та str(3).

a="3"
print 'The first case: "3" * 7 =', a*7
print 'The second case: 3 * 7 =', 3*7
print 'Conversation int("3") =', int("3")
print 'Conversation str(3) =' , str(3)

print '\n ========= Task 5 ========='
#5.	Що станеться, коли стрічки форматування %6s та %-6s використовується для відображення стрічки довшої ніж 6 символів?
print '6 spaces before:','%6s' % 'str'
print '6 spaces after:','%-6s' % 'str'

#Якщо введена стрічка має менше 6 символів, то вихідна стрічка доповнена пробілами до довжини 6 символів і значення змінної вирівняне по правому краю (%6s)
#або по лівому краю(%-6s).
#Коли ж ми використовуємо %6s або %-6s та стрічку довшу ніж 6 символів, то з стрічкою нічого не відбувається.

print '\n ========= Task 7 ========='
#7. Створіть файл, який буде містити слова та їх частоту записані в окремих рядках через пробіл ( fuzzy 53). Прочитайте цей файл використовуючи
# open(filename).readlines().  Розділіть кожну стрічку на дві частини використовуючи split(),і перетворіть число в ціле значення використовуючи int().
#Результат повинен бути у вигляді списку: [['fuzzy', 53], ...].

file = open('E:\doc.txt')
p=file.readlines()
print p
a=[]
for i in p:
    c=i.split()
    a.append([i.split()[0],int(i.split()[1])])

print '\n ========= Task 10 ========='
# Модуль random включає функцію choice(), яка випадковим чином вибирає елементи послідовності. Наприклад, choice("aehh ") буде вибирати один з чотирьох символів.
#Напишіть програму генерації стрічки з 500 випадково вибраних символів "aehh ".
#Для поєднання елементів в стрічку використовуйте ''.join() . Нормалізуйте отриманий результат використовуючи split() та join().
import random
aa=''
for i in range(500):
    aa=aa+''.join(random.choice("aehh "))
print  aa[:50]
bb=aa.split()
print bb[:15]


print '\n ========= Task 13 ========='
13.	Використовуючи Porter стемер нормалізуйте будь-який токенізований текст . До того самого тексту застосуйте Lancaster стемер.
Результати порівняйте та поясніть.

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
#14.	Доступіться до текстів ABC Rural News та ABC Science News з корпуса (nltk.corpus.abc).
#Знайдіть значення для оцінки читабельності текстів (аналогічно до задачі №12).
#Використовуйте Punkt для поділу тексту на окремі речення.

from nltk.corpus import abc
l=0
n=0
for w in nltk.corpus.abc.words():
    l+=len(w)
    n+=1
    mw = l/n #середня к-сть літер у слові
print mw
ms = len(nltk.corpus.abc.words()) / len(nltk.corpus.abc.sents())#середнє значення к-сті слів у реченні в тексті 
print ms
ari = 4.71*mw+0.5*ms-21.43# визначаю міру оцінки читабельності за цим виразом
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








