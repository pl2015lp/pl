# -*- coding: utf-8 -*-

print "task3"
# Опрацювати всі приклади з методичних вказівок по роботі зі словниками. Що станеться, якщо доступитися до неіснуючого запису звичайного словника та словника по замовчуванню?
import nltk
pos={'colorless':'ADJ', 'ideas': 'N', 'sleep': 'V', 'furiously': 'ADV'}
print pos
print pos ['night']
# якщо доступитися до неіснуючого запису звичайного словника, то вибиває помилку.

pos=nltk.defaultdict(list)
print pos['blog']

pos=nltk.defaultdict(lambda: 'V')
print pos['google']
#у випадку зі словником за замовчуванням слово автоматично додається до словника.

print "task7"
# Використовуючи sorted() та set() отримайте відсортований список всіх тегів корпуса Brown без їх дублювання.
import nltk, re, pprint
from nltk.corpus import brown
def tag_list (tagged_words):
	tags=[]
	for (w,t) in tagged_words:
		tags.append(t)
	tags_list=set(tags)
	return pprint.pprint (sorted(tags_list))
print tag_list(nltk.corpus.brown.tagged_words())

print "task11" 
#Напишіть програму, яка обробить Brown Corpus і допоможе відповісти на наступне запитання: які теги для маркування іменників найчастіше використовуються і що вони означають.
import nltk
brown=nltk.corpus.brown.tagged_words()
def findtag(tags, text):
	tag_list=[]
	for tag in text:
		if tag[1].startswith(tags):
			tag_list+=[tag[1]]
	fd=nltk.FreqDist(tag_list)
	print 'Noun tags', (tags,len(set(tag_list)))
	print 'All:', fd.keys()
	return 'The most frequent:', fd.keys()[:5]
print findtag('N',brown)

print "task13"
#Напишіть програму для збору статистичних даних по розмічених корпусах і відповіді на наступне запитання: скільки слів мають неоднозначності в змісті того, що маркуються двома і більше тегами; 
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

print "task 18"
#Напишіть програми для знаходження слів та словосполучень згідно відповідних їм тегів для відповіді на наступне питання: яке співвідношення між займенниками (чоловічими і жіночими).
from nltk import FreqDist, ConditionalFreqDist
from nltk.corpus import brown
fd = FreqDist()
cfd = ConditionalFreqDist()
for sentence in brown.tagged_sents():
    for (token, tag) in sentence:
        fd.inc(tag)
        cfd[token].inc(tag)
male = ['he','his','him','himself'] 
female = ['she','hers','her','herself'] 
n_male, n_female = 0, 0
for m in male:
    n_male += cfd[m].N()
for f in female:
    n_female += cfd[f].N()
print float(n_male)/n_female

print "task21"
#Написати програму побудови словника, записами якого будуть набори словників. Використовуючи створений словник, збережіть у ньому набори можливих тегів, які зустрічаються після заданого слова з певним тегом, наприклад wordi → tagi → tagi+1. 
import nltk
from nltk.corpus import brown
pos=nltk.defaultdict(lambda: nltk.defaultdict(int))
btags=brown.tagged_words(simplify_tags=True)
for ((w1, t1), (w2, t2)) in nltk.bigrams(btags):
    pos [(w1, t1)][t2] += 1

print pos [('curly', 'ADJ')]
print pos [('spring', 'N')]
