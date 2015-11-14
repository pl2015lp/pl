# -*- coding: utf-8 -*-
import nltk
from nltk import*

import random, string

"""
3.	Створити список списків слів
[ [‘’,’’,’’… ], [[‘’,’’,’’…  ], [[‘’,’’,’’…],…]
(наприклад текст складається з речень, які складаються з стрічок).
Здійснити операцію присвоювання text2 = text1[:],
та здійснити операцію присвоювання нового значення одному зі слів
(text1[1][1] = 'Monty').
Перевірити як ці операції вплинули на text2. Результат письмово пояснити
"""
print "\n3)\n"
a = "First list of words".split()
b = "Second list of words".split()
c = "Third list of words.".split()
text1=[a, b, c]

text2=text1[:]
text1[1][1]='>>Monty<<'
print text1
print text2
"""
текст2 також змінився
[['First', 'list', 'of', 'words'], ['Second', '>>Monty<<', 'of', 'words'], ['Third', 'list', 'of', 'words.']]
[['First', 'list', 'of', 'words'], ['Second', '>>Monty<<', 'of', 'words'], ['Third', 'list', 'of', 'words.']]

"""

"""
5.Створити список списків пустих стрічок використовуючи множення списків,
наприклад word_table = [[''] * n] * m.
Що станеться, якщо встановити одне зі значень такого списку,
наприклад word_table[1][2] = "hello"?
Пояснити письмово отримані результати.
Створіть аналогічний список використовуючи функцію range()
і продемонструйте що такий список позбавлений такого недоліку
при присвоєнні значення одному з його елементів
"""
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


"""
11. Гематрія – метод виявлення прихованого змісту слів
на основі порівняння чисел, які відповідають словам.
Слова з однаковими числами мають однаковий зміст.
Число слова визначається сумуванням чисел, як відповідають його літерам.
Написати функцію decode() для обробки тексту,
яка випадковим чином замінює слова на їх Гематрія-еквіваленти.
Чи вдалося виявити "прихований зміст" тексту?
(Використовувати letter_vals з попередньої задачі)
"""

print "\n11\n"


def decode (text):
    letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
    new_text = text.lower().split()
    s = 0
    word = random.choice(new_text)
    print "word: %s" % (word)
    for w in letter_vals.keys():
        if w in word:
            s = s + letter_vals[w]
    for i in new_text:
        if i == word:
            new_text[new_text.index(i)] = str(s)
    print string.join (new_text)


decode("Some random text in my lab. work")

"""
лол
"""

"""
14.	Написати функцію, яка обробляє список слів (з дублюванням слів)
і повертає список слів (без дублювання) відсортований в порядку спадання їх частоти.
"""

print "\n14)\n"

def frSort(text):
    fr=nltk.FreqDist(text)
    print fr
    return fr.keys()


str1='word1 word3 word4 word4 word4 word2 word2 word4 word3 word3'
print frSort(str1.split())

"""
<FreqDist: 'word4': 4, 'word3': 3, 'word2': 2, 'word1': 1>
['word4', 'word3', 'word2', 'word1']
"""
                
"""
16. Імпортувати функцію itemgetter() модуля operator
зі стандартної бібліотеки Python ( from operator import itemgetter).
Створити список words , який містить декілька слів.
Спробувати виконати: sorted(words, key=itemgetter(1)),
та sorted(words, key=itemgetter(-1)).
Пояснити письмово роботу функції itemgetter().
"""
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


"""

17.	В NLTK реалізовано алгоритм Левінштейна для порівняння стрічок.
Спробуйте скористатись цим модулем nltk.edit_dist().
Яким чином в цьому модулі використовується динамічне програмування?
Який підхід використовується знизу-вверх чи зверху-вниз? Пояснити письмово. 

"""
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


