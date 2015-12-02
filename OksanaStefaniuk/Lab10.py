﻿# -*- coding: cp1251 -*-

import nltk, re, pprint
from nltk.corpus import brown

#Task1
#Здійсніть тренування юніграм аналізатора на основі частини корпуса, який відповідає першій або другій літері прізвища студента та виконайте аналіз тексту з частини корпуса, яка відповідає першій або другій літері імені студента. Результати поясніть.
#Чому для деяких слів не встановлені теги.

print "\n1)\n"

print brown.categories()
brown_tagged_sents=brown.tagged_sents(categories='learned')
brown_sents=brown.sents(categories='learned')
unigram_tagger=nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(brown_sents[30])
print 'Punctuation marks have no tags'
print unigram_tagger.evaluate(brown_tagged_sents)
brown_tagged_sents_1=brown.tagged_sents(categories='adventure')
brown_sents_1=brown.sents(categories='adventure')
unigram_tagger.tag(brown_sents_1[30])
print unigram_tagger.evaluate(brown_tagged_sents_1)
t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(brown_tagged_sents, backoff=t0)
print t1.evaluate(brown_tagged_sents)
print t1.evaluate(brown_tagged_sents_1)

#Task2
#Здійсніть тренування біграм аналізатора на частинах корпуса з вправи 3.1 без backoff аналізатора.
#Перевірте його роботу.
#Що відбулося з продуктивністю аналізатора? Чому?

print "\n3)\n"

brown_tagged_sents=brown.tagged_sents(categories='adventure')
bigramm_tagger=nltk.BigramTagger(brown_tagged_sents, cutoff=0)
brown_sents=brown.sents(categories='adventure')[30]
print bigramm_tagger.tag(brown_sents)
print bigramm_tagger.evaluate(brown_tagged_sents)


#Task3
#Дослідити наступні проблеми, що виникають при роботі з аналізатором на основі підстановок:
#що відбудеться з продуктивністю аналізатора, якщо опустити backoff аналізатор (дослідити на частині броунівського корпусу,
#яка відповідає першій або другій літері прізвища студента);
#на основі рис.1. та відповідного фрагмента програми встановити точку максимальної продуктивності незважаючи на розмір списку (об’єм оперативної пам’яті)
#і точку достатньої продуктивності при мінімальному розмірі списку.

print "\n4)\n"

fd=nltk.FreqDist(nltk.corpus.brown.words(categories='learned'))
most_freq_words=fd.keys()[:30]
print most_freq_words
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='learned'))
possible_tags=dict((w, cfd[w].max()) for w in most_freq_words)
uni_tagger=nltk.UnigramTagger(model=possible_tags, backoff=nltk.DefaultTagger('NN'))
uni_tagger.tag(nltk.corpus.brown.sents(categories='learned')[30])
uni_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='learned'))
uni_tagger=nltk.UnigramTagger(model=possible_tags)
uni_tagger.tag(nltk.corpus.brown.sents(categories='learned')[30])
uni_tagger.evaluate(nltk.corpus.brown.tagged_sents(categories='learned'))
def performance(cfd, wordlist):
	a=dict((w, cfd[w].max()) for w in wordlist)
	uni_tagger=nltk.UnigramTagger(model=a, backoff=nltk.DefaultTagger('NN'))
	return uni_tagger.evaluate(brown.tagged_sents(categories='learned'))
def display():
	import pylab
	words_by_freq=list(nltk.FreqDist(brown.words(categories='learned')))
	cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='learned'))
	sizes =2**pylab.arange(15)
	p=[performance(cfd, words_by_freq[:size]) for size in sizes]
	pylab.plot(sizes, p, '-bo')
	pylab.title('Tagger and its size')
	pylab.xlabel('Model Size')
	pylab.ylabel('Performance')
	pylab.show()	
print display()

#Task4
#Знайдіть розмічені корпуси текстів для інших мов які вивчаєте або володієте (українська, польська, німецька, російська, італійська, японська).
#Здійсніть тренування та оцініть продуктивність роботи різних аналізаторів та комбінацій різних аналізаторів.
#Точність роботи аналізаторів порівняйте з точністю роботи аналізаторів для англійських корпусів.
#Результати поясніть.

print "\n5)\n"

fd= nltk.FreqDist(nltk.corpus.conll2002.words ())
a= fd.keys()[:50]
print a
cfd= nltk.ConditionalFreqDist(nltk.corpus.conll2002.tagged_words())
b= dict((w, cfd[w].max()) for word in a)
print b['voor']
print b['ha']
print b['La']
unigram_tagger= nltk.UnigramTagger (model=b)
unigram_tagger.evaluate(nltk.corpus.conll2002.tagged_sents())
c= nltk.corpus.conll2002.tagged_sents ()
t0= nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(c, backoff=t0)
t2=nltk.BigramTagger(c, cutoff=0, backoff=t1)
t2.evaluate(c)
from nltk.corpus import treebank
d=nltk.corpus.treebank.tagged_sents()
t0= nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(d, backoff=t0)
t2=nltk.BigramTagger(d, cutoff=0, backoff=t1)
t2.evaluate(d)


#Task5
#Створити аналізатор по замовчуванню та набір юніграм і n-грам аналізаторів.
#Використовуючи backoff здійсніть тренування аналізаторів на частині корпуса з вправи 3.2.
#Дослідіть три різні комбінації поєднання цих аналізаторів.
#Перевірте точність роботи аналізаторів.
#Визначіть комбінацію аналізаторів з максимальною точністю аналізу.
#Змініть розмір даних на яких проводилось тренування.
#Повторіть експерименти для змінених даних для тренування.
#Результати порівняйти і пояснити.


print "\n6)\n"

a = nltk.corpus.brown.tagged_sents(categories='learned')
sent = nltk.corpus.brown.sents(categories='learned')[2000]
afsize=[-1,-2,-3]
for i in afsize:
	nltk.AffixTagger(a,affix_length=i, min_stem_length=3).tag(sent)
b = nltk.corpus.brown.tagged_sents(categories='adventure')
sent = nltk.corpus.brown.sents(categories='adventure')[1000]
afsize=[-1,-2,-3,-4,-5]
for i in afsize:
	nltk.AffixTagger(b, affix_length=i, min_stem_length=3).tag(sent)
default_tagger=nltk.DefaultTagger('NN')
unigram_tagger=nltk.UnigramTagger(a)
bigram_tagger = nltk.BigramTagger(a, cutoff=0)
affix_tagger = nltk.AffixTagger(a, affix_length=-2, min_stem_length=3)
t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(a, backoff=t0)
t2=nltk.BigramTagger(a, backoff=t1)
t3=nltk.AffixTagger(a, backoff=t2)
print t3.evaluate(a)
print t3.evaluate(b)
t0=nltk.UnigramTagger(a, backoff=t0)
t1=nltk.BigramTagger(a, backoff=t1)
t2=nltk.AffixTagger(a, backoff=t2)
t3=nltk.DefaultTagger('NN')
print t3.evaluate(a)
print t3.evaluate(b)
t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(a, backoff=t0)
t2=nltk.AffixTagger(a, backoff=t1)
t3=nltk.BigramTagger(a, backoff=t2)
print t3.evaluate(a)
print t3.evaluate(b)


#Task6
#Прочитати стрічку документування функції demo Brill аналізатора.
#Здійснити експерименти з різними значення параметрів цієї функції.
#Встановити який взаємозв’язок є між часом тренування (навчання аналізатора) і точністю його роботи.

print "\n7)\n"

from nltk.book import*
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.80000000000000004, trace=3)
print 'Result: Training unigram tagger: [accuracy: 0.832151], Training bigram tagger: [accuracy: 0.837930], Training Brill tagger on 1600 sentences... Found 9757 useful rules.'

#Task7
#Прочитати файл допомого про морфологічний аналізатор на основі афіксів (help(nltk.AffixTagger)). Напишіть програму, яка викликає аналізатор на основі афіксів в циклі, з різними значеннями довжини афіксів і мінімальними довжинами слів.
#При яких значеннях можна отримати кращі результати.

print "\n2)\n"

brown_a = nltk.corpus.brown.tagged_sents(categories='adventure')
sent = nltk.corpus.brown.sents(categories='adventure')[289]
afsize=[-1,-2,-3]
stem_size=[2,3]
for i in afsize:
	for j in stem_size:
		tagger=affix_tagger=nltk.AffixTagger(brown_a,affix_length=i,min_stem_length=j)
		analyze=tagger.tag(sent)
		evaluation=tagger.evaluate(brown_a)
		print analyze
		print tagger
		print evaluation
print 'The best result is when the affix length=-2 and the min stem length=0'
