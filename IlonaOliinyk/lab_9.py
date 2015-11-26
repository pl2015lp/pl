# -*- coding: utf-8 -*-
"""
3.	Опрацювати всі приклади з методичних вказівок по роботі зі словниками.
Що станеться, якщо доступитися до неіснуючого запису звичайного словника
та словника по замовчуванню?
"""
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
"""
I: PRP
a: DT
cat: N
have: V
"""
simple = dict()
simple['night']
"""
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    pos['night']
KeyError: 'night'
"""
default = nltk.defaultdict(str)
default['night'] #''
"""
Якщо доступитися до неіснуючого запису звичайного словника, отримаємо помилку.
Натомість, словник по замовчуванню створить новий запис і присвоїть
йому пусте/нульове значення, або значення за замовчуванням, якщо таке вказане.
"""

"""
Спробуйте видалити запис зі словника d, використовуючи del d['abc'].
"""
pos = {}
pos['I'] = 'PRP'
pos['have'] = 'V'
pos['a'] = 'DT'
pos['cat'] = 'N'
print pos
del pos['a']
print pos
#{'I': 'PRP', 'a': 'DT', 'have': 'V', 'cat': 'N'}
#{'I': 'PRP', 'have': 'V', 'cat': 'N'}
#5.	Створити два словники
#Що станеться зі словниками після виконання команди d1.update(d2)
import nltk

dictionary1={'yellow':'ADJ','white':'ADJ'}
dictionary2={'school':'N','university':'N'}
dictionary1.update(dictionary2)
print dictionary1
print dictionary2
"""
dictionary1
{'university': 'N', 'white': 'ADJ', 'school': 'N', 'yellow': 'ADJ'}
dictionary2
{'school': 'N', 'university': 'N'}
dictionary2 has not changed
"""
"""
7.Використовуючи sorted() та set() отримайте відсортований список всіх
тегів корпуса Brown без їх дублювання.
"""
print '\n7)\n'
import nltk
brown = nltk.corpus.brown.tagged_words()

def tag(text):
    tag_list = []
    for tags in text:
        tag_list += [tags[1]]
    print "The number of tags id : %d" % (len(set(tag_list)))
    return sorted(list(set(tag_list)))[:200]

print ">>"
print tag(brown)
#Сет щоб не було повторів
"""Сортед сортує """


"""
Напишіть програму, яка обробить Brown Corpus і допоможе відповісти
на наступне запитання: які іменники частіше зустрічаються
у множині ніж в однині (розглядати тільки регулярні форми множини).
"""
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
"""
2-year-olds: 3
aberrations: 5
abolitionists: 4
aborigines: 8
absolutes: 3
"""
"""
Напишіть програму для збору статистичних даних по розмічених корпусах і відповіді на наступне
запитання: скільки слів мають неоднозначності в змісті того, що маркуються двома і більше тегами.
"""
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
not_one_tag ()
#5393

#Напишіть програми для знаходження слів та словосполучень згідно відповідних
#їм тегів для відповіді на наступне питання: які слова можуть бути іменниками
#(множина) або дієсловами (третя особа однини)(deals, flies)?

print '\n17)\n'
import nltk
from nltk.corpus import brown

words_tagged = brown.tagged_words()
cfd = nltk.ConditionalFreqDist(words_tagged)
print [w for w in cfd.conditions() if 'NNS' in cfd[w] and 'VBZ' in cfd[w]] [:50]
#VBZ: verb, present tense, 3rd person singular\ NNS: noun, common, plural
#Якщо вважати теги – умовою та слова подією,
#то можна встановити слова, які найчастіше маркуються певним тегом

"""
21. Написати програму побудови словника, записами якого будуть
набори словників. Використовуючи створений словник, збережіть
у ньому набори можливих тегів, які зустрічаються
після заданого слова з певним тегом, наприклад wordi → tagi → tagi+1.
"""


print '\n21)\n'
kp = nltk.corpus.brown.tagged_words()

def search(word, tag):
    x = dict()
    y = nltk.defaultdict(dict)
    z = []
    for i in range(len(kp)-1):
        d = kp[i]
        e = kp[i+1]
        if d[0] == word and d[1] == tag:
            z += [e[1]]
    x[tag] = set(z)
    y[word] = x
    return y

print ">>"
print search('now', 'RB')
print search ('something', 'NN')



