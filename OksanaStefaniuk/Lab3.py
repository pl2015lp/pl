# -*- coding: utf8 -*-
import nltk
from nltk.book import *

#)Task2
#Напишіть, використовуючи модуль читання корпусу текстів Brown nltk.corpus.brown.words(), програму, яка дозволяє доступитися до фрагментів текстів
#у двох різних жанрах корпусу Brown,і назва яких відповідає першій літері прізвища і імені студента.
print "\n1)"
from nltk.corpus import brown
print brown.words (categories=['science_fiction'])
print brown.words (categories=['lore'])

#Task6
#Проаналізуйте таблицю частот модальних дієслів для різних жанрів.
#Спробуйте її пояснити. Знайдіть інші класи слів вживання яких також відрізняються в різних жанрах.
print "\n2)"
cfd=nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres=['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals=['can', 'could', 'may', 'might', 'must', 'will', 'beautiful', 'home']
cfd.tabulate(conditions=genres,samples=modals)

#Task7
#Напишіть програму для знаходження всіх слів в корпусі Brown, які зустрічаються не менш ніж три рази.
print "\n3)"
from nltk.corpus import brown
words_all = brown.words()
fdist = nltk.FreqDist(words_all)
fdist = nltk.FreqDist([w.lower() for w in all_words])
for m in all_words:
    if fdist[m] > 3:
        print m + ':', fdist[m]

#Task10
#Напишіть програму яка виводить на екран 50 найчастотніших біграмів тексту, за виключенням біграмів до складу яких входять незначущі слова.
print "\n4)"
from nltk.corpus import gutenberg
gutenberg.fileids()
text1=gutenberg.words('austen-persuasion.txt')
stopwords=nltk.corpus.stopwords.words('english')
t=([w.lower() for w in text1])
bigrams=nltk.bigrams(t)
fdist= nltk.FreqDist([bi for bi in bigrams if bi[0] not in stopwords and bi[1] not in stopwords])
print fdist.keys()[:50]

        
#Task12
#Напишіть функцію word_freq(), яка приймає слово і назву частини корпуса Brown як аргументи і визначає частоту слова в заданій частині корпуса.
print "\n5)"
import nltk
from nltk.corpus import brown
def word_freq(word, section):
    freq = nltk.probability.FreqDist(nltk.corpus.brown.words(categories = section))
    word_frequency = freq[word]
    return word_frequency

m=word_freq('under','news')
n=word_freq('day', 'news')
print 'freq of word \'under\' in news section of Brown corpus: %s\t'%(m)
print 'freq of word \'day\' in news section of Brown corpus: %s\t'%(n)

#Task8
#Напишіть програму генерації таблиці відношень  кількість слів/кількість оригінальних слів для всіх жанрів корпуса Brown.
#Проаналізуйте отримані результати та поясніть їх.
print "\n6)"
from nltk.corpus import brown
for genre in brown.categories():
    num_words = len(brown.words(categories=genre))
    num_vocab = len(set([w.lower() for w in brown.words(categories=genre)]))
    print num_words/num_vocab, genre

