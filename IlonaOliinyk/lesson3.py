# -*- coding: utf-8 -*-

import nltk


#Використовуючи конкорданси поясніть відмінності у вживанні
#слова however на початку речення
#("in whatever way", "to whatever extent", або "nevertheless”).

print "\n4)\n"
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
print emma.concordance("However")


#Проаналізуйте таблицю частот модальних дієслів для різних жанрів.
#Спробуйте її пояснити. Знайдіть інші класи слів
#вживання яких також відрізняються в різних жанрах.

print "\n6)\n"
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
  (genre, word)
   for genre in brown.categories()
       for word in brown.words(categories=genre))
words = ['can', 'could', 'may', 'might', 'must', 'will',
        'under','on', 'in', 'at','upon',
         'with','by']
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
cfd.tabulate(conditions=genres, samples=words)



#Напишіть програму для знаходження всіх слів в корпусі Brown,
#які зустрічаються не менш ніж три рази.

print "\n7)\n"


print '\nFrequency of word appearance in Brown corpus:\n'
text = brown.words()
fdist = nltk.FreqDist([w.lower() for w in text])
counter = 1;

for m in text:
    #слова, які зустрічаються
    #не менше ніж 3 рази і не коротші 3 символів.
    if fdist[m] > 3 and len(m) > 3: 
        print "[%s] %s : %s" % (counter,m, fdist[m])
        if counter == 40:
            break
        counter = counter + 1


#Напишіть програму генерації таблиці відношень  кількість
#слів/кількість оригінальних слів для всіх жанрів корпуса Brown.
#Проаналізуйте отримані результати та поясніть їх.

print "\n8)\n"

print 'Ratio of the general amount of words to the general amount of original words'
print "=========================================="
for genre in brown.categories():
    #Кількість слів у і-тій категорії
    num_words = len(brown.words(categories=genre))
    #Кількість оригінальних слів і-тої категорії
    num_vocab = len(set([w.lower() for w in brown.words(categories=genre)]))
    print "|Genre: %s - %s" %    (genre, int(num_words/num_vocab))
print "=========================================="



#Напишіть програму для створення таблиці частот слів для різних жанрів.
#Знайдіть слова чия присутність або відсутність є характерною для певних жанрів
#(подібно до модальних дієслів).

print "\n11)\n"
adjectives = ['good', 'bad', 'awesome', 'light', 'heavy', 'important']

#for genre in brown.categories():
#   text = brown.words(categories=genre)
#   fdist = nltk.FreqDist([w.lower() for w in text])
#   for word in adjectives:
#      print "[%s] %s : %s" % (genre,word,fdist[word])


cfd = nltk.ConditionalFreqDist(
  (genre, word)
   for genre in brown.categories()
       for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
cfd.tabulate(conditions=genres, samples=adjectives)




#Визначити функцію hedge(text),
#яка обробляє текст і створює нову версію цього тексту
#додаючи слово ‘like’ перед кожним третім словом.

print "\n13)\n"

from nltk.book import text1

#Створюємо функцію.
def hedge(text):
    count = 1
    textRes = ""
    for w in text:
        if count < 3:
            textRes += w + " "
            if w.isalpha():
                count += 1
        else:
        #Якщо лічильник дорівнює 3, то додаємо слово 'like' перед 3-ім словом
            count = 1
            textRes += "[like] "
        
    return textRes


#Додаємо слово 'like' у новий текст у проміжку від 100 до 130 слова
new_text = hedge(text1[100:130])
print "\nNew Text:\n"
print new_text



