# -*- coding: utf-8 -*-
from __future__ import division
import urllib, nltk
from urllib import urlopen

print "task1"
# Напишіть функцію, яка приймає адресу URL, як аргумент, і повертає те, що міститься за цією адресою з видаленням HTML розмітки. Використовувати urllib.urlopen для доступу до контенту наступним чином raw_contents=urllib.urlopen('http://www.nltk.org/').read().
url="http://www.nltk.org/"
raw_contents=urllib.urlopen(url).read()
raw=nltk.clean_html(raw_contents)
tokens=nltk.word_tokenize(raw)
print tokens 




print "task2"
# Збережіть деякий текст у файл corpus.txt. Визначити функцію load(f) для читання файлу, назва якого є її аргументом і повертає стрічку, яка містить текст з фалую 
def load(f):
    a=open(f)
    raw=a.read()
    return raw
print



print "task3"
# Перепишіть наступний цикл як list comprehension:
sent = ['the', 'dog', 'gave', 'John', 'the', 'newspaper']
result=[]
for word in sent:
    word_len = (word, len(word))
    result.append(word_len)
print result 
sent = ['The', 'dog', 'gave', 'John', 'the', 'newpaper']
print [(word, len(word)) for word in sent]



print "task4"
# Перевірити різницю між стрічками і цілим виконавши наступні дії: "3" * 7 та 3 * 7. Спробуйте здійснити конвертування між стрічками і цілими використавши int("3") та str(3). 
print '3' * 7
print 3 * 7
print int("3") * 7  
print str(3) * 7



print "task5"
# Що станеться, коли стрічки форматування %6s та %-6s використовується для відображення стрічки довшої ніж 6 символів?
print '%6s' % 'catcatcat'
print '%6s' % 'cat' 
print '%-6s' % 'catcatcatcat' 
print '%-6s' % 'cat' 




print "task6"
# Прочитайте деякий текст з корпуса, здійсніть його токенізацію і збережіть у список всі wh-слова, які в ньому зустрічаються.  
from nltk.corpus import gutenberg
print gutenberg.fileids() 
a=gutenberg.raw('austen-persuasion.txt')
tokens=nltk.word_tokenize(a)
wh_words=[w.lower() for w in tokens if w.startswith ('wh')]
print wh_words[:40]


print"task7"
# Створіть файл, який буде містити слова та їх частоту записані в окремих рядках через пробіл ( fuzzy 53).  Прочитайте цей файл використовуючи open(filename).readlines(). Розділіть кожну стрічку на дві частини використовуючи split(), і перетворіть число в ціле значення використовуючи int(). Результат повинен бути у вигляді списку: [['fuzzy', 53], ...].
f=open('C:\Python27\TASK_7.txt').readlines()
print f
for line in f:
    print line.split() 

for line in f:
    print line.split()

for line in f:
    sp=[]
    s=line.split()
    s[1]=int(s[1])
    sp+=s

print sp




print"task12"
# Міра оцінки читабельності використовується для оцінки складності тексту для читання. Нехай uw-середня кількість літер у слові, та us - середнє значення кількості слів у реченні в певному тексті. Automated Readability Index(ARI) тексту визначається згідно виразу: 4.71 uw + 0.5 us - 21.43. Визначити значення ARI для різних частин корпуса Brown Corpus, включаючи частину f (popular lore) та j (learned). Використовуйте nltk.corpus.brown.words() для знаходження послідовності слів та nltk.corpus.brown.sents() для знаходження послідовності речень.

import nltk
from nltk.corpus import brown
print brown.categories()


num_chars=len(brown.raw(categories='lore'))
num_words=len(brown.words(categories='lore'))
num_sents=len(brown.sents(categories='lore'))
Rw=int(num_chars/num_words)
print Rw
Rs=int(num_words/num_sents)
print Rs
ARI=4.7*Rw+0.5*Rs-21.43
print ARI

num_chars=len(brown.raw(categories='learned'))
num_words=len(brown.words(categories='learned'))
num_sents=len(brown.words(categories='learned'))
Rw=int(num_chars/num_words)
print Rw
Rs=int(num_words/num_sents)
print Rs
ARI=4.7*Rw+0.5*Rs-21.43
print ARI



print "task15"
# Перепишіть наступний цикл, як list comprehension:
words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = set()
for word in words:
    vowels = []
    for char in word:
        if char in 'aeiou':
            vowels.append(char)
    vsequences.add(''.join(vowels))
print sorted(vsequences)


words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = set()
[vsequences.add(''.join(vowels)) for vowels in [char for char in word if char in 'aeiou']]
print sorted (vsequences)
              




