# -*- coding: utf-8 -*-

#Task1
#Знайти в Python's help додаткову інформацію про послідовності.
#В інтерпретаторі, набрати по черзі help(str), help(list), та help(tuple).
#На екрані буде відображено повний список функцій властивих кожному з типів.
#Деякі функції мають спеціальні імена з подвійними підкреслюваннями.
#Кожній такій функції відповідає і інший запис показаний  в документації.
#Наприклад x.__getitem__(y) відповідає x[y].

print "1\n"
print help(str)
print help(list)
print help(tuple)

#Task2
#Знайти три операції, які можна здійснювати і зі списками та із
#кортежами. Знайти три операції, які не можна здійснювати над кортежами.
#Знайдіть коли використання списку замість кортежу приводить до Python помилки.

print "\n2\n"
list1 = ['Oksana','Stefaniuk']
tuple1 = ('Oksana','Stefaniuk')

print list1 + ['Volodymyrivna']
print tuple1 + ('Volodymyrivna',)

tuple2 = ('I','am')
tuple2+=tuple1
print tuple2

list2 = ['I','am']
list2 +=list1
print list2

print list1 * 4
print tuple1 * 4

print list1[0]
print tuple1[0]

print len(list1)
print len(tuple1)

#Знайдіть коли використання списку замість кортежу приводить до Python помилки.
         

#del tuple1[0]
print tuple1
#'tuple' object doesn't support item deletion
tuple1.append('1')
print tuple1
#'tuple' object has no attribute 'append'
tuple1.sort()
print tuple1
#'tuple' object has no attribute 'sort'



#Task3.Яким чином можна створити кортеж з одного елемента.
#Продемонструвати два різні способи.

print "\n3)\n"

tuple3 = ('Oksana',)
print tuple3 
tuple4='Oksana',
print tuple4

#Task4.Написати програму для коректного виділення
#в тексті n-грамів з врахуванням граничних випадків: n = 1, та n = len(sent)?

print "\n4)\n"
import nltk
sent="I have never ever been to London. So, it was difficult for me to get to the city centre."

def ngram(f,n):
    a=nltk.word_tokenize(f)
    b=nltk.ngrams(a,n)
    return b

print ngram(sent,1)
print "\n"
print ngram(sent,3)
print "\n"
print ngram(sent,len(sent))


#Task5 'Monty' < 'Python'. Що станеться, якщо виконати  'Z' < 'a'?
#Порівняти стрічки,як мають однаковий префікс, наприклад 'Monty' < 'Montague'.
#Спробувати порівняти структуровані
#об’єкти ,наприклад. ('Monty', 1) < ('Monty', 2). Чи отримали очікувані результати?
print "\n5)\n"
         
#по алфавіту.  true
print 'Monty'<'Python'
#велкі букви є менші за значенням  A-Z a-z  true
print 'Z'<'a'
# Monta  іде перед Monty,тому false
print 'Monty' < 'Montague'
# Monty = Monty, 1 < 2 true
print ('Monty', 1) < ('Monty', 2)
# Букви у словах порівнюються відносто своєї позиції в алфавіті,
#меншою є та буква, яка стоїть вище по алфавіту.


#task6 Написати програму видалення пробілів на початку і вкінці стрічки та для
#видалення зайвих пробілів між словами.
#Використовувати split() та join(). Оформити у вигляді функції.
#Функція повинна містити повну стрічку документування.
print "\n6)\n"
         
def OddSpace(a):
	'This function deletes needless spaces and the spaces at the beginning and at the end of the sentence'
	f=' '.join(a.split())
	return f
b='I have never ever been to London. So, it was difficult for me to get to the city centre.    '
print OddSpace(b)


#Task7.Написати програму видалення пробілів на початку і в кінці стрічки та для видалення зайвих пробілів між словами.
#Використовувати re.sub() . Оформити у вигляді функції. Функція повинна містити повну стрічку документування.

print "\n7)\n"

import re
def OddSpace(a):
	'This function deletes needless spaces and the spaces at the beginning and at the end of the sentence'
	f=re.sub('\s+', ' ',a)
	ff=re.sub('^\s|\s$','',f)
	return ff

b='   I have never ever been to London. So, it was difficult for me to get to the city centre.  '
print OddSpace(b)


#Task8.Написати програму сортування слів за їх довжиною. Визначити допоміжну функцію cmp_len, яка буде
#використовувати функцію  cmp для порівняння довжин слів.
#Функція повинна містити повну стрічку документування.

print "\n8)\n"
         
def cmp_len (a,b):
	'This function compares the words lengths'
	if cmp(len(a), len(b)) < 0:
		a,b=b,a #якщо перший елемент менший за другий, то переставляємо їх місцями
	return [a,b]
    
def sort(f):
	'This function sorts the words by their lengths'
	for j in range(len(f)):
		for i in range(len(f)):
			f[i], f[j] = cmp_len(f[i], f[j])
	return f

sent = "I have never ever been to London. So, it was difficult for me to get to the city centre.".split()
print sort(sent)
