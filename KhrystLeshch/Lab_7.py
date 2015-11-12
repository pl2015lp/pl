# -*- coding: utf-8 -*-
print "task1"
# Знайти в Знайти в Python's help додаткову інформацію про послідовності. В інтерпретаторі,набрати по черзі help(str), help(list), та help(tuple). На екрані буде відображено повний список функцій властивих кожному з типів. Деякі функції мають спеціальні імена з подвійними підкреслюваннями. Кожній такій функції відповідає і інший запис показаний  в документації. Наприклад x.__getitem__(y) відповідає x[y].

print help (str) 
print help (list) 
print help (tuple) 

print "task2"
# Знайти три операції, які можна здійснювати і зі списками та із кортежами. Знайти три операції, які не можна здійснювати над кортежами. Знайдіть коли використання списку замість кортежу приводить до Python помилки.
kortezh = (2, 10, 3, 'hello', 'autumn', 'november')
spysok=[2, 10, 3, 'hello', 'autumn', 'november']
print len (kortezh) 
print len(spysok)  
print kortezh*2 
print spysok*2 
print 2 in kortezh 
print 'hello' in spysok 
del(kortezh[0])
kortezh.append('go')
kortezh.sort()


print "task3"
# Яким чином можна створити кортеж з одного елемента. Продемонструвати два різні способи.
kortezh = ('go',)
print kortezh 
kortezh1='evening',
print kortezh1



print "task4"
# Створити список words = ['is', 'NLP', 'fun', '?']. Використовуючи операції присвоювання подібні до words[1] = words[2] та тимчасову змінну  tmp перетворити цей список в список ['NLP', 'is', 'fun', '!']. Здійснити аналогічні перетворення використовуючи присвоювання в кортежах.
words = ['is', 'NLP', 'fun', '?']
tmp=words[0]
words[0] = words[1]
words[1] = tmp
words[3] = '!'
print words
words = ['is', 'NLP', 'fun', '?']
tmp='!'
print (words[1], words[0], words[2], tmp)


print "task5"
# Прочитати про вбудовану функцію здійснення порівнянь cmp, набравши help(cmp). Продемонструвати чим поведінка цієї функції відрізняється від поведінки операторів порівняння.
print help (cmp) 
x=1
y=2
print cmp(x,y) 
print x>y  
print x<y 
x=10
y=10
print cmp(x,y) 
x=10
y=2
print cmp(x,y) 

print "task6"
# Написати програму для коректного виділення в тексті n-грамів з врахуванням граничних випадків: n = 1, та n = len(sent)?
sent = 'Audentes fortuna iuvat'
s=sent.split()
print s 
n=1
print [s[i:i+n] for i in range (len(s)-n+1)] 
n=len(s)
print [s[i:i+n] for i in range (len(s)-n+1)] 


print "task7"
# Використати оператори нерівності для порівняння стрічок, наприклад. 'Monty' <'Python'. Що станеться, якщо виконати  'Z' < 'a'? Порівняти стрічки,як мають однаковий префікс, наприклад 'Monty' < 'Montague'. Спробувати порівняти структуровані об’єкти ,наприклад. ('Monty', 1) < ('Monty', 2). Чи отримали очікувані результати?
print 'Monthy'<'Python'
print 'Z'<'a' 
print 'Monty'<'Montague' 
print ('Monty', 1)<('Monty', 2) 


print "task8"
# Написати програму видалення пробілів на початку і в кінці стрічки та для видалення зайвих пробілів між словами. Використовувати split() та join(). Оформити у вигляді функції. Функція повинна містити повну стрічку документування.
sent = 'Audentes fortuna iuvat'
def clean (sent):
    words=sent.split()
    words=' '.join(words)
    return words


print "task9"
# Написати програму видалення пробілів на початку і в кінці стрічки та для видалення зайвих пробілів між словами. Використовувати re.sub() . Оформити у вигляді функції. Функція повинна містити повну стрічку документування
import re
sent = 'Audentes  fortuna  iuvat '
def clean (sent):
    sent = re.sub("^\s+","", sent)
    sent = re.sub("\s+$","", sent)
    sent = re.sub("\s(2)"," ", sent)
    return sent




print "task10"
# Написати програму сортування слів за їх довжиною. Визначити допоміжну функцію cmp_len, яка буде використовувати функцію  cmp для порівняння довжин слів. Функція повинна містити повну стрічку документування.
def cmp_len(word1, word2):
    return cmp (len(word1),len(word2))
def sort_words(sent):
    words=sent.split()
    words.sort(lambda word1, word2: cmp_len(word1, word2))
    print words 
sent = 'Audentes  fortuna  iuvat '
print sort_words(sent)
