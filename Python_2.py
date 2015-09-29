#3.1. Створіть змінну sentence і присвойте їй значення ‘she sells sea shells by the sea shore’ та напишіть фрагмент програми для виведення на екран всіх слів які починаються з ‘sh’.
sentence = 'she sells sea shells by the sea shore'
words = sentence.split()
for i in words:
    if i.startswith('sh'):
        print i
 
#3.4. Напишіть програму, яка видаляє всі голосні зі стрічки, яка відповідає імені, по батькові та прізвищу студента. Програма повинна здійснювати наступну послідовність дій: створення початкової стрічки; створення стрічки, у якій буде зберігатися результат; for цикл для обробки стрічки символ за символом і запису неголосних символів в результуючу стрічку.
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
 
#3.7. Виконати наступні приклади і пояснити чому отримані різні результати (різні значення змінних) 
sorted(set([w.lower() for w in text1]))
sorted([w.lower() for w in set(text1)])
	
#3.13. Перевірте виконання виразу set(sent3) < set(text1). Змініть аргументи функції. Результати поясніть.
import nltk
from nltk.book import*

if set(sent3) < set(text1):
    print 'true'
else:
    print 'false'
 
#Речення меньше за розміром ніж цілий текст. 

#3.11. Напишіть вираз для знаходження в тексті №6 всіх слів які відповідають наступним вимогам: закінчуються на ize; містять літеру z; містять послідовність літер pt; написані з великої літери . Результат представити, як список слів.
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
 
#3.15. Побудуйте колокації для текстів №1 та №4. Результати порівняйте.
import nltk
from nltk.book import*
print text1.collocations()
print text4.collocations()
 
