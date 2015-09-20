# -*- coding: utf-8 -*-
# Створіть змінну sentence і присвойте їй значення 'she sells sea shells by the sea shore' та напишіть фрагмент програми, яка генерує нову стрічку додаючи 'like' перед кожним зі слів, яке починається з 'se'.
sentence = 'she sells sea shells by the sea shore'
sentence1 = sentence.split()
sentence1
for word in sentence1:
	if word.startswith ('se'):
		print 'like ' + word


# Напишіть програму для перевірки наявності в стрічці sent = 'colorless green ideas sleep furiously' окремих слів та підстрічокю

sent ='colorless green ideas sleep furiously'
words = sentence.split()
words

for word in words:
	print word

'she'.startswith ('sh')
'le' in words
'colorless'.endswith ('s')
'green'.endswith ('s')
for word in words:
	if word.endswith ('s'):
		print word

word[:]

import nltk
from nltk.book import*

sorted ([w for w in set(text7) if '-' in w and 'index' in w])  # команда виводить на екран слова, які вживаються з словом index

sorted ([wd for wd in set(text3) if wd.istitle() and len(wd) > 10])  # команда перевіряє чи в тексті3 є слова з великої лутери. які мають більше ніж 10 # 

sorted ([w for w in set(sent7) if not w.islower() ])# В сьомому реченні які слова починаються з великої літери

sorted ([t for t in set(text2) if 'cie' in t or 'cei' in t]) # команда визначає слова, які мають cie чи cei.

V = set (text1)
long_words = [w for w in V if len(w) > 15]
sorted (long_words)

sorted(set([w.lower() for w in text1])) # у цьому випадку кількість слів менше через те, що set  вжито перед умовою і порахувало без повторів.

V = set (text2)
long_words = [w for w in V if len(w) > 20]
sorted (long_words)




V = set (text8)
long_words = [w for w in V if len(w) > 17]
sorted (long_words)

# У другому тексті немає слів більших за 20. У третьому є слова, які мають більше, ніж 12 символів. Результат залежить від довжини слова та тексту.


# Використайте вираз sum([len(w) for w in text1])
sum([len(w) for w in text1])

# Перевірте виконання виразу set(sent3( < set(text1). Змініть аргумент функції. Результати поясніть.
set(set3)<set(text1) # set3 не розпізнаний аргумент. міняю set3 на text3, і довжина третього тексту не є меншою ніж довжина першого.

set(text3)<set(text1) 

#Виконати наступні приклади і пояснити чому отримані різні результати (різні значення змінних)
sorted(set([w.lower() for w in text1])) # умова set вжита перед умовою і тому воно рахувало без повторів
sorted([w.lower() for w in set(text1)])


# Побудуйте колокацій для текстів №1 та №9. Результати порівняйте.
text1.collocations()
s=[len(w) for w in text1]
fdist = FreqDist ([len(w) for w in text1])
fdist
fdist.keys()
fdist.items()
fdist.max()
fdist[3]
fdist.freq(3)


text9.collocations()
s=[len(w) for w in text1]
fdist = FreqDist ([len(w) for w in text9])
fdist
fdist.keys()
fdist.items()
fdist.max()
fdist[3]
fdist.freq(3)

# Найчастіше зустрічаються слова довжиною 3 символи, але у другому випадку частота їхньої появи більша.


              

