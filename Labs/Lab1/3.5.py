Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Використовуючи зрізи та операцію поєднання змінити стрічку msg до вигляду ім’я , по батькові, прізвище студента.
>>> msg = "OlhaTurchyniak"
>>> msg = msg [0:4] + ' ' + 'Ivanivna' + ' ' + msg[4:14]
>>> msg
'Olha Ivanivna Turchyniak'
>>> 
