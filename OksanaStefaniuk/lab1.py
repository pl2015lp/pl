# -*- coding: cp1251 -*-
import nltk
from nltk.book import *
#Task1
#�������� ����� msg �������� �� �������� ������, ��� ������� ���� �� ������� ��������.
print "\n1)"
msg='Oksana Stefaniuk'
print msg

#Task9
#���������� ������ �� �������� ������ � ���������� ������. ���������� �������.
print "\n2)"
print msg[8:14:2]



#Task10
#������� ��������� ��������� msg[::-1].
print "\n3)"
print 'The msg is printed in reversed order: ' + msg[::-1]
print msg[-1:-17:-1]

#Task11
#����������� �������, ��� �� �� ������� �� ������ ������. �������� ��������� �������� ������������, ���������� �� ����.
#��������� �������� ������� �� ������� �������� ������ �� �������� � ����.
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
#�������� ������ phrase1, ���� ���������� �� ������� ��� , �� �������, ������� ��������.
#�� ���������� ��� ����� ������ � ������������� ��������� �������� phrase1[2][2]. ������� ���������.
print "\n5)"
phrase1 = [nam, pb, pr]
print phrase1
print phrase1[2][2]

#Task24
#������������ ������� index() ��������� ����� �inexpressible�.index(�e�).
#�� ��������� ���� �������� �inexpressible�.index(�re�)
print "\n6)"
str2 = 'inexpressible'
print 'Symbol \'e\' has index - ' + str(str2.index('e'))
print 'Symbols \'re\' have index of the inicial symbol \'r\' - ' + str(str2.index('re'))

#Task25
#��������� ������� ��� ��� � ������ phrase1 �������������� ����� index().
print "\n7)"
for word in phrase1:
    print "[%d] %s" % (phrase1.index(word), word)
