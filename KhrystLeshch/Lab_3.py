# -*- coding: utf-8 -*-
# Напишіть, використовуючи модуль читання корпусу текстів Brown nltk.corpus.brown.words(), програму, яка дозволяє доступитися до фрагментів тектсів у двох різних жанрах корпусу Brown, і назва яких відповідає першій летері прізвища та імені студента.

import nltk
from nltk.corpus import brown
brown.categories()
brown.words ( categories = ['learned', 'humour'])
brown.sents (categories = ['lore', 'humour'])
brown.sents (categories = ['learned', 'humour'])




#Проаналізуйте таблицю частот модальних дієслів для різних жанрів. Спробуйте її пояснити. Знайдіть інші класи слів вживання яких також відрізняється в різних жанрах.
from nltk.corpus import brown
brown.categories()
cfd = nltk.ConditionalFreqDist(
	(genre, word)
	for genre in brown.categories()
	for word in brown.words(categories=genre))
genres = ['news', 'hobbies', 'humour', 'government', 'mystery']
prepositions = ['for', 'in', 'at', 'by', 'on', 'behind', 'after']
cfd.tabulate(conditions=genres, samples=prepositions)


# Напишіть програму для знаходження всіх слів в корпусі Brown, які зустрічаються не менше ніж три рази.

from nltk.corpus import brown
slowa_all = brown.words()
fdist = nltk.FreqDist(slowa_all)
fdist

fdist = nltk.FreqDist([w.lower() for w in slowa_all])
for m in slowa_all:
	if fdist[m] > 3:
		print m + ':', fdist[m]



# Напишіть програму генерації таблиці відношень кількість слів/кількість оригінальних слів для всіх жанрів корпуса Brown. Проаналізуйте отримані результати та поясніть їх.
for genre in brown.categories():
	num_words = len(brown.words(categories=genre))
	num_vocab = len(set([w.lower() for w in brown.words(categories=genre)]))
	print int (num_words/num_vocab), genre

# Визначити функцію hedge(text), яка обробляє текст і створює нову версію цього тексту додаючи слово 'like' перед кожним третім словом.
import nltk
from nltk.book import*
def hedge(text):
	textResult=''
	counter=0
	for w in text:
		if counter == 2:
			counter =0
			textResult=textResult + '[like]'+' ' +w +' '
			counter+=1
		else:
			textResult=textResult+' ' +w
			counter= counter+1
	return textResult
newText = hedge(text1[:50])
print newText

