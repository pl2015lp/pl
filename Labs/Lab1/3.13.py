Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Представити прізвище, ім’я та по батькові як список стрічок. Використовуючи метод .reverse() та зріз [::-1] змінити стрічку. Результати пояснити.
>>> 
>>> msg = ['Turchyniak', 'Olha', 'Ivanivna']
>>> msg
['Turchyniak', 'Olha', 'Ivanivna']
>>> msg1 = msg.reverse()
>>> msg
['Ivanivna', 'Olha', 'Turchyniak']
>>> msg1
>>> ['Ivanivna', 'Olha', 'Turchyniak'] [::-1]
['Turchyniak', 'Olha', 'Ivanivna']
>>> 
# метод reverse() міняє місцями списки стрічок без зміни у них символів з кінця на початок, а зріз [::-1] повертає списки у початкове положення.
