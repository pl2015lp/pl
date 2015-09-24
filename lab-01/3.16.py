#Створити змінну words яка містить список слів. Дослідіть операції words.sort() i sorted(words)

words = ["hi", "my", "buy", "son"]
print words
['hi', 'my', 'buy', 'son']
# функція sorted повертає відсортований масив,
# не змінюючи при цьому заданий масив"
print sorted(words)
['buy', 'hi', 'my', 'son']
print words
['hi', 'my', 'buy', 'son']
# метод sort() модифікує масив від якого його викликали
words.sort()
print words
['buy', 'hi', 'my', 'son']
