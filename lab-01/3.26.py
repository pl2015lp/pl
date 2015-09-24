#визначіть змінну silly, яка буде містити стрічку "newly formed bland ideas are inexpressible in an infuriating way" і 
напишіть програму її перетворення в список phrase,який буде містити всі слова silly крім "in"


silly = "newly formed bland ideas are inexpressible in an infuriating way"

# заміняємо всі "in" на ""
silly = silly.replace("in", "")

# розбиваємо стрічку на масив стрічок беручи за розділювач пробіл
words = silly.split(" ")

print words
['newly', 'formed', 'bland', 'ideas', 'are', 'expressible', '', 'an', 'furiatg', 'way']
