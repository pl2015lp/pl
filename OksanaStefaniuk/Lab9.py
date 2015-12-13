# -*- coding: utf-8 -*-

#Task1
#Токенізувати та здійснити морфологічний аналіз наступного речення:
#They wind back the clock, while we chase after the wind.
#Які відмінності у вимові слів пов’язані з їх морфологічними характеристиками.

print "\n1)\n"

import nltk
text=nltk.word_tokenize('They wind back the clock, while we chase after the wind.')
print nltk.pos_tag(text)

#Task2
#Опрацювати всі приклади з методичних вказівок по роботі зі словниками.
#Що станеться, якщо доступитися до неіснуючого запису звичайного словника та словника по замовчуванню?

print "\n3)\n"

pos = {}
pos['I'] = 'PRP'
pos['have'] = 'V'
pos['a'] = 'DT'
pos['cat'] = 'N'
print pos #{'I': 'PRP', 'a': 'DT', 'have': 'V', 'cat': 'N'}
pos['have'] #'V'
print len(pos) #4
print list(pos) #['I', 'a', 'have', 'cat']
print sorted(pos) #['I', 'a', 'cat', 'have']
print [w for w in pos if w.endswith('t')] #['cat']
for word in sorted(pos):
print word + ':', pos[word]

I: PRP
a: DT
cat: N
have: V

simple = dict()
simple['night']

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pos['night']
KeyError: 'night'

default = nltk.defaultdict(str)
default['night'] #''


#Якщо доступитися до неіснуючого запису звичайного словника, отримаємо помилку.
#Натомість, словник по замовчуванню створить новий запис і присвоїть
#йому пусте/нульове значення, або значення за замовчуванням, якщо таке вказане.



#Task4
#Спробуйте видалити запис зі словника d, використовуючи del d['abc'].

print "\n4)\n"

d = {'I':'PRO','like':'V','to':'TO','learn':'V','English':'N'}
print d
del d['I']
print d
del d ['like']
print d


#Task5
#Використовуючи sorted() та set() отримайте відсортований список всіх тегів корпуса Brown без їх дублювання.

print "\n7)\n"

import nltk
brown = nltk.corpus.brown.tagged_words()
def tag(text):
    tag_list = []
    for tags in text:
        tag_list += [tags[1]]
print "The number of tags id : %d" % (len(set(tag_list)))
return sorted(list(set(tag_list)))[:200]

print tag(brown)

#Сортед сортує 
#Сет щоб не було повторів

#Task6
#Напишіть програму, яка обробить Brown Corpus і допоможе відповісти на наступне запитання:
#які іменники частіше зустрічаються у множині ніж в однині (розглядати тільки регулярні форми множини).

print "\n8)\n"

import nltk
from nltk.corpus import brown
def plural_nouns():
    nouns = [word.lower() for (word,tag) in brown.tagged_words(simplify_tags=True) if tag=='N']
    fdist = nltk.FreqDist(nouns)
    dict_nouns = {}
    for word in nouns:
        if word.endswith('s'):
            dict_nouns[word]=word[:-1]
    results = []
    for plural,singular in dict_nouns.iteritems():
        if fdist[plural]>fdist[singular] and fdist[singular]>0:
    results.append(plural)
    for word in nltk.FreqDist(results).keys():
print word + ': %i' % fdist[word]
print plural_nouns

#Task7
#Напишіть програму для збору статистичних даних по розмічених корпусах і відповіді на наступне запитання:
#скільки слів мають неоднозначності в змісті того, що маркуються двома і більше тегами; 


print "\n13)\n"

import nltk
from nltk.corpus import brown
def create_dict():
    tag_count = nltk.defaultdict(list)
    for (word,tag) in brown.tagged_words(simplify_tags=True):
        if tag not in tag_count[word.lower()]:
            tag_count[word.lower()].append(tag)
    return tag_count
def not_one_tag():
    dict_tags = create_dict()
    n = 0
    for word in dict_tags:
        if len(dict_tags[word])>=2 and word.isalpha():
            n=n+1
print n
print not_one_tag ()

#Task8
#Напишіть програми для знаходження слів та словосполучень згідно відповідних їм тегів для відповіді на наступне питання:
#які слова можуть бути іменниками (множина) або дієсловами (третя особа однини)(deals, flies);

print "\n17)\n"

import nltk
from nltk.corpus import brown

words_tagged = brown.tagged_words()
cfd = nltk.ConditionalFreqDist(words_tagged)
print [w for w in cfd.conditions() if 'NNS' in cfd[w] and 'VBZ' in cfd[w]] [:50]

#VBZ: verb, present tense, 3rd person singular\ NNS: noun, common, plural
#Якщо вважати теги – умовою та слова подією,
#то можна встановити слова, які найчастіше маркуються певним тегом

#Task9
#Написати програму побудови словника, записами якого будуть набори словників. Використовуючи створений словник,
#збережіть у ньому набори можливих тегів, які зустрічаються після заданого слова з певним тегом, наприклад wordi → tagi → tagi+1.

print "\n21)\n"

import nltk
from nltk.corpus import brown
pos=nltk.defaultdict(lambda: nltk.defaultdict(int))
btags=brown.tagged_words(simplify_tags=True)
for ((w1, t1), (w2, t2)) in nltk.bigrams(btags):
    pos [(w1, t1)][t2] += 1

print pos [('curly', 'ADJ')]
print pos [('spring', 'N')]
