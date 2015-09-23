silly = "newly formed bland ideas are inexpressible in an infuriating way"

# заміняємо всі "in" на ""
silly = silly.replace("in", "")

# розбиваємо стрічку на масив стрічок беручи за розділювач пробіл
words = silly.split(" ")

print words
