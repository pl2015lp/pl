# -*- coding: utf-8 -*-
from __future__ import division

#1.	Напишіть функцію, яка приймає адресу URL, як аргумент,
#і повертає те що міститься за цією адресою з видаленням HTML розмітки.
#Використовувати urllib.urlopen для доступу до контенту наступним чином
#raw_contents = urllib.urlopen('http://www.nltk.org/').read().
print "\n1)\n"

import urllib, nltk
from urllib import urlopen

def HTMLtoString(url):
    html = urlopen(url).read()
    string = nltk.clean_html(html)
    #Для подальшої роботи з текстом потрібно розділити текст
    #на окремі слова та виділити розділові знаки.
    #Такий процес називають токенізацією. 
    tokens = nltk.word_tokenize(string)
    #print "\n3)"
    return tokens


url = "http://www.nltk.org/"
someString = HTMLtoString(url)
print someString[0:140]


#2. Збережіть деякий текст у файлі corpus.txt. Визначити функцію load(f) для читання файлу,
#назва якого є її аргументом і повертає стрічку, яка містить текст з файлу.

print "\n2)\n"


def load1(filename):
	f = open(filename, 'rU')
	f1 = f.read()
	return f1


filepath = "path/textForlab5.txt"
someString1 = load1(filepath)
print someString1[0:200]

#3

print "\n3)\n"
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
result = []
for word in sent:
    word_len = (word, len(word))
    result.append(word_len)

print result

result1 = [(word, len (word)) for word in sent]
print result1

#4.Перевірити різницю між стрічками і цілим виконавши наступні дії: "3" * 7 та 3 * 7.
#Спробуйте здійснити конвертування між стрічками і цілими використавши int("3") та str(3).

print "\n4)\n"

var1 = "3" * 7 # сім раз вивести 3
var2 = 3 * 7 #21
var3 = int("3")*7   #21
var4 = str(3) * 7   # сім раз вивести 3

print ">1:\t%s" % (var1)
print ">2:\t%s" % (var2)
print ">3:\t%s" % (var3)
print ">4:\t%s" % (var4)


#5.	Що станеться, коли стрічки форматування %6s та %-6s
#використовується для відображення стрічки довшої ніж 6 символів?

print "\n5)\n"

str1 = "word"
str2 = "String bigger then 6 characters"

#Якщо рядок менший від вказаної к-ті символів, то він доповнюється пропусками
# на місці відсутніх символів

print ">1:%10s"  % (str1)
print ">2:%-10s" % (str1)

print ">3:%50s"  % (str2)
print ">4:%-50s" % (str2)



#7. Створіть файл, який буде містити слова та їх частоту записані в окремих
#рядках через пробіл ( fuzzy 53).
#Прочитайте цей файл використовуючи open(filename).readlines().
#Розділіть кожну стрічку на дві частини використовуючи split(),
#і перетворіть число в ціле значення використовуючи int().
#Результат повинен бути у вигляді списку: [['fuzzy', 53], ...].
print "\n7)\n"

filename = "path/lab5_words.txt"

myList = []

f = open(filename).readlines()
for line in f:
    word = line.split()[0]
    intVariable = int(line.split()[1])
    lineList = [word, intVariable]
    myList.append(lineList)
    
print myList



#12.	Міра оцінки читабельності використовується для оцінки складності тексту для читання.
#Нехай, μw - середня кількість літер у слові, та μs – середнє значення кількості слів у реченні в певному тексті.
#Automated Readability Index (ARI) тексту визначається згідно виразу: 4.71 μw + 0.5 μs - 21.43.
#Визначити значення ARI для різних частин корпуса Brown Corpus, включаючи частину f (popular lore) та j (learned).
#Використовуйте nltk.corpus.brown.words() для знаходження послідовності слів та nltk.corpus.brown.sents() для знаходження послідовності речень
print "\n12)\n"


from nltk.corpus import brown
print brown.categories()

def fun(category):
   print category
   num_chars = len(brown.raw(categories=category))
   num_words = len(brown.words(categories=category))
   num_sents = len(brown.sents(categories=category))
   Uw = int(num_chars/num_words)
   Us = int(num_words/num_sents)
   ARI=4.7*Uw+0.5*Us-21.43
   print "Us = %s, Uw = %s, ARI = %s" % (Us, Uw, ARI)
   

fun('lore')
fun('learned')


#for categ in brown.categories():
#    fun(categ)


#15.	Перепишіть наступний цикл, як list comprehension:
print "\n15)\n"

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']

vsequences = set()
for word in words:
    vowels = []
    for char in word:
        if char in 'aeiou':
            vowels.append(char)
            vsequences.add(''.join(vowels))


#print vsequences
print sorted(vsequences)


print ">>>>>\t\t\ 2nd method>>>>\t"
[vsequences.add(''.join(vowels)) for vowels in [char for char in word if char in 'aeiou']]
print sorted (vsequences)



#8. Напишіть програму доступу до вебсторінки
#і вилучення з неї деякого тексту.
print "\n8)\n"

url = raw_input("Enter URL: ")

someString = HTMLtoString(url)
print someString[0:140]



