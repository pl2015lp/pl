# -*- coding: utf-8 -*-
import nltk
from nltk import*

import random, string

#Task1
#Створити список слів і зберегти їх в змінній sent1.
#Здійснити операцію присвоювання sent2 = sent1[:].
#Змінити один з елементів в sent1 і перевірити чи змінився sent2.
#Результат письмово пояснити.

print "\n2)\n"

sent1=['Fifty', 'shades', 'of', 'grey', '.']
sent2=sent1[:]
print sent2
sent1[1]='shades'
print sent1
print sent2
print 'sent2 did not change its meaning, because changes were provided after the equation'

#Task2
#Створити список списків пустих стрічок використовуючи множення списків, наприклад word_table = [[''] * n] * m.
#Що станеться, якщо встановити одне зі значень такого списку, наприклад word_table[1][2] = "hello"?
#Пояснити письмово отримані результати. Створіть аналогічний список використовуючи функцію range()
#і продемонструйте що такий список позбавлений такого недоліку при присвоєнні значення одному з його елементів. 

print "\n5)\n"

col = 4
row = 3
word_table = [[' '] * col] * row
word_table[1][2] = "hello"
print word_table

"""
Присвоюємо другій колонці слово Хелоу для всіх рядківі!
[['', '', 'hello', ''],
['', '', 'hello', ''],
['', '', 'hello', '']]
"""
word_range = []

for i in range(row):
    word_range.append([""]*col)

word_range[1][2] = "hello"
print word_range

"""
Присвоюємо другій колонці, першому стовпцю слово Хелоу!
[['', '', '', ''],
['', '', 'hello', ''],
['', '', '', '']]
"""

#Task3
#Гематрія – метод виявлення прихованого змісту слів на основі порівняння чисел, які відповідають словам.
#Слова з однаковими числами мають однаковий зміст.
#Число слова визначається сумуванням чисел, як відповідають його літерам.
#Здійснити аналіз корпусу (наприклад nltk.corpus.state_union).
#Для кожного з текстів визначити скільки слів мають номер 555 та 777.
#(Використовувати letter_vals з попередньої задачі)

print "\n10)\n"

import nltk, re, pprint, string
from string import ascii_lowercase
letter_vals={'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8, 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
def gematria555and777(text):
	tokens=nltk.word_tokenize(text)
	count=0
	s=[]
	words=[]
	for token in tokens:
		sum=0
		word_list=list(token)
		if token not in s:
			s.append(token)
			for letter in word_list:
				if letter in string.ascii_lowercase:
					sum+=letter_vals[letter]
		if sum==555 or sum==777:
			count+=1
			words.append(token)
	return count
from nltk.corpus import state_union
for fileid in state_union.fileids():
	w=gematria555and777(string.lower(state_union.raw(fileid)))
	print w, fileid


#Task4
#Написати list comprehension для сортування списку синсетів WordNet за близькістю до заданого синсету.
#Наприклад, дані синсети  minke_whale.n.01, orca.n.01, novel.n.01, та tortoise.n.01, потрібно їх відсортувати згідно їх path_distance() від right_whale.n.01.

print "\n13)\n"

from nltk.corpus import wordnet as wn
right_whale=wn.synset('right_whale.n.01')
synsets=['minke_whale.n.01', 'orca.n.01', 'novel.n.01', 'tortoise.n.01']
for i in synsets:
	list_sim=[]
	w1=right_whale
	w2=wn.synset(i)
	similarity=w1.path_similarity(w2)
	list_sim.append((i,similarity))
	sorted(list_sim)

#Task5
#Імпортувати функцію itemgetter() модуля operator
#зі стандартної бібліотеки Python ( from operator import itemgetter).
#Створити список words , який містить декілька слів.
#Спробувати виконати: sorted(words, key=itemgetter(1)),
#та sorted(words, key=itemgetter(-1)).
#Пояснити письмово роботу функції itemgetter().

print "\n16)\n"

from operator import itemgetter
print ">>"
#str2 = "Some words in this string"
#str2 = "abc ccc baa bbb aaa"
str2 = "abc bba aab bbc acb"
words = str2.split()
print sorted(words, key=itemgetter(0))
print sorted(words, key=itemgetter(1))
print sorted(words, key=itemgetter(2))

"""
#itemgetter() tells sorted()
which index in a word to use while sorting the list of the words
['abc', 'aab', 'acb', 'bba', 'bbc']
['aab', 'abc', 'bba', 'bbc', 'acb']
['bba', 'aab', 'acb', 'abc', 'bbc']
"""

#Task6
#NLTK реалізовано алгоритм Левінштейна для порівняння стрічок.
#Спробуйте скористатись цим модулем nltk.edit_dist().
#Яким чином в цьому модулі використовується динамічне програмування?
#Який підхід використовується знизу-вверх чи зверху-вниз? Пояснити письмово. 

import nltk
print "\n17)\n"
print nltk.edit_distance("Ilona", "Beer")#5
print nltk.edit_distance("Viber", "Viper")#1
print nltk.edit_distance("software", "hardware")#4
print nltk.edit_distance("never", "ever")#1
"""
В цьому модулі використовується динамічне програмування, адже процес вирішення
завдання складається з певних етапів. Використовується підхід знизу вверх,
спочатку визначається довжина стрічок, а потім відстань редагування між ними.
"""


