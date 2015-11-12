# -*- coding: utf-8 -*-
print "task3"
# Створити список списків слів [ [‘’,’’,’’… ], [[‘’,’’,’’…  ], [[‘’,’’,’’…],…] (наприклад текст складається з речень, які складаються з стрічок). Здійснити операцію присвоювання text2 = text1[:], та здійснити операцію присвоювання нового значення одному зі слів (text1[1][1] = 'Monty'). Перевірити як ці операції вплинули на text2. Результат письмово пояснити.
text1=[['My', 'name', 'is', 'Khrystyna', '.'],['My', 'surname', 'is', 'Leshchyshyn', '.']]
text2=text1[:]
text1[1][1]='Monty'
print text1
print text2

# Змінна text2 не змінилась, бо рядок text2=text1[:] означає копіювання вмісту змінної.

print "task11"
# Гематрія – метод виявлення прихованого змісту слів на основі порівняння чисел, які відповідають словам. Слова з однаковими числами мають однаковий зміст. Число слова визначається сумуванням чисел, як відповідають його літерам. Написати функцію decode() для обробки тексту, яка випадковим чином замінює слова на їх Гематрія-еквіваленти. Чи вдалося виявити "прихований зміст" тексту? (Використовувати letter_vals з попередньої задачі)
import nltk
text='Per aspera ad astra'
def decode (text):
    import random, string
    s=0
    text_n=text.lower().split()
    word=random.choice(text_n)
    letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8, 'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100, 'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}
    for w in letter_vals.keys():
        if w in word:
            s=s+letter_vals[w]
    for i in text_n:
        if i==word:
            text_n[text_n.index(i)]=str(s)
            print string.join(text_n)


print "task14"
# Написати функцію, яка обробляє список слів (з дублюванням слів) і повертає список слів (без дублювання) відсортований в порядку спадання їх частоти.
import nltk
from nltk import*
def sortuvannia(text):
    text=nltk.FreqDist(text.lower().split())
    return text.keys()
t='Per aspera ad astra'
print sortuvannia(t)


print "task16"
# Імпортувати функцію itemgetter() модуля operator зі стандартної бібліотеки Python (from operator import itemgetter). Створити список words , який містить декілька слів. Спробувати виконати: sorted(words, key=itemgetter(1)), та sorted(words,key=itemgetter(-1)). Пояснити письмово роботу функції itemgetter().
from operator import itemgetter
words=['per', 'aspera', 'ad', 'astra']
print sorted(words, key=itemgetter(1))
print sorted(words, key=itemgetter(-1))
# Функція itemgetter(index) використовується з функцією sorted() і тому відбувається сортування слв за літерою, що вказана як index.

print "task17"
# В NLTK реалізовано алгоритм Левінштейна для порівняння стрічок. Спробуйте скористатись цим модулем nltk.edit_dist(). Яким чином в цьому модулі використовується динамічне програмування? Який підхід використовується знизу-вверх чи зверху-вниз? Пояснити письмово.
import nltk
print help(nltk.edit_distance)
print nltk.edit_distance('luck', 'love')
# відстань Левінштайна обраховує відстань між двома стрічками, використовуючи підхід знизу-вверх.
