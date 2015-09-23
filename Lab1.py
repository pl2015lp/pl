"""3.2 Роздрукувати вміст змінної msg двома шляхами, перший набравши назву змінної в інтерпретаторі, другий - використавши команду print."""
msg = 'Olena Stetskiv'
msg
print msg

"""3.10 Поясніть результат виконання msg[::-1]."""
msg[::-1]

"""3.5 Використовуючи зрізи та операцію поєднання змінити стрічку msg до вигляду ім’я , по батькові, прізвище студента."""
msg[0:5] + ' Olehivna ' + msg[6:]

"""3.12 Представити прізвище, ім’я та по батькові як список стрічок. Розділити речення на окремі елементи, межа розділу голосна буква."""
msg.split('e')

"""3.16 Створити змінну words яка містить список слів. Дослідіть операції words.sort() і sorted(words)."""
words = ['one', 'two', 'three', 'four', 'five']
words

sorted(words)
words

words.sort()
words

"""	3.25 Визначіть позиції всіх слів в списку phrase1 використовуючи метод index()."""
phrase1 = ['Monday', 'Wednesday', 'Friday', 'Sunday']
phrase1

phrase1.index('Friday')

phrase1.index('Monday')

phrase1.index('Wednesday')

phrase1.index('Sunday')

for word in phrase1:
	print word, phrase1.index(word)

""" 3.26 Визначіть змінну silly, яка буде містити стрічку ’newly formed bland ideas are inexpressible in an infuriating way’ і напишіть програму її перетворення в список phrase, який буде містити всі слова silly крім ‘in’."""
silly ='newly formed bland ideas are inexpressible in an infuriating way'
silly

phrase =[]
for word in silly.split():
	if word != 'in':
		phrase.append(word)

phrase

