# -*- coding: cp1251 -*-
import nltk
from nltk.book import *
#Task1
#Створити змінну msg присвоїти їй значення стрічки, яка відповідає імені та прізвищу студента.
print "\n1)"
msg='Oksana Stefaniuk'
print msg

#Task9
#Організуйте доступ до елементів стрічки з визначеним кроком. Результати поясніть.
print "\n2)"
print msg[8:14:2]



#Task10
#Поясніть результат виконання msg[::-1].
print "\n3)"
print 'The msg is printed in reversed order: ' + msg[::-1]
print msg[-1:-17:-1]

#Task11
#Представити прізвище, ім’я та по батькові як список стрічок. Здійснити різноманітні операції індексування, сортування та зрізів.
#Реалізуйте операцію доступу до окремих елементів списку та операцій з ними.
print "\n4)"
nam=msg[0:6]
print nam
pr = msg[7:16]
print pr
pb='Volodymyrivna'
msg = pr + ' ' + nam + ' ' + pb
print msg
msg_list = [pr, nam, pb]
print msg_list
print len(msg_list)
print msg_list[0]
print msg_list[-1]
print msg_list[1]
print msg_list[2]
print msg_list[0:1]
print msg_list[0:3]
msg_list1 = msg_list[1] + msg_list[2]
print msg_list1
msg_list1 = msg_list[1] + ' ' + msg_list[2]+ ' ' + msg_list[0]
print msg_list1
msg_list.sort()
print msg_list
msg_list.reverse()
print msg_list
print msg_list.index('Oksana')

#Task15
#Створити список phrase1, який складається із значень ім’я , по батькові, прізвище студента.
#Що відбудеться при спробі ввести в інтерпретатор наступний оператор phrase1[2][2]. Поясніть результат.
print "\n5)"
phrase1 = [nam, pb, pr]
print phrase1
print phrase1[2][2]

#Task24
#Використайте функцію index() наступним чином ’inexpressible’.index(’e’).
#Що станеться якщо виконати ’inexpressible’.index(’re’)
print "\n6)"
str2 = 'inexpressible'
print 'Symbol \'e\' has index - ' + str(str2.index('e'))
print 'Symbols \'re\' have index of the inicial symbol \'r\' - ' + str(str2.index('re'))

#Task25
#Визначіть позиції всіх слів в списку phrase1 використовуючи метод index().
print "\n7)"
for word in phrase1:
    print "[%d] %s" % (phrase1.index(word), word)
