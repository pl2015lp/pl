#3.1. ������� ����� sentence � ��������� �� �������� �she sells sea shells by the sea shore� �� �������� �������� �������� ��� ��������� �� ����� ��� ��� �� ����������� � �sh�.
sentence = 'she sells sea shells by the sea shore'
words = sentence.split()
for i in words:
    if i.startswith('sh'):
        print i
 
#3.4. �������� ��������, ��� ������� �� ������ � ������, ��� ������� ����, �� ������� �� ������� ��������. �������� ������� ���������� �������� ����������� ��: ��������� ��������� ������; ��������� ������, � ��� ���� ���������� ���������; for ���� ��� ������� ������ ������ �� �������� � ������ ���������� ������� � ����������� ������.
name1 = 'Bilyk Dmytro Haiyovich'
name2 = ''
for i in name1:
    if 'a' not in i:
        name2+=i
name1=''
for i in name2:
   if 'o' not in i:
        name1+=i
name2=''
for i in name1:
    if 'i' not in i:
        name2+=i
name1=''
for i in name2:
    if 'u' not in i:
        name1+=i
name2=''
for i in name1:
    if 'y' not in i:
        name2+=i
print name2
 
#3.7. �������� ������� �������� � �������� ���� ������� ��� ���������� (��� �������� ������) 
sorted(set([w.lower() for w in text1]))
sorted([w.lower() for w in set(text1)])
	
#3.13. �������� ��������� ������ set(sent3) < set(text1). ����� ��������� �������. ���������� �������.
import nltk
from nltk.book import*

if set(sent3) < set(text1):
    print 'true'
else:
    print 'false'
 
#������� ������ �� ������� �� ����� �����. 

#3.11. �������� ����� ��� ����������� � ����� �6 ��� ��� �� ���������� ��������� �������: ����������� �� ize; ������ ����� z; ������ ����������� ���� pt; ������� � ������ ����� . ��������� �����������, �� ������ ���.
import nltk
from nltk.book import*
result1 = sorted([w for w in set(text6) if w.endswith('ize')])
for word in result1:
    print word
    print '=========================================='
result2 = sorted([w for w in set(text6) if 'z' in w])
for word in result2:
    print word
print '=========================================='
result3 = sorted([w for w in set(text6) if 'pt' in w])
for word in result3:
    print word
print '=========================================='
result4 = sorted([w for w in set(text6) if w.istitle()])
for word in result4:
    print word
 
#3.15. ��������� ��������� ��� ������ �1 �� �4. ���������� ���������.
import nltk
from nltk.book import*
print text1.collocations()
print text4.collocations()
 
