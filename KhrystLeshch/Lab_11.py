# -*- coding: utf-8 -*-


#В класі Tree реалізовано різноманітні корисні методи. Переглянути файл допомоги  Tree з документації та описати основні з цих методів (import Tree,  help(Tree).
print "task2"
import nltk
from nltk import Tree
print help(Tree)


print "task4"
#Перетворити всі дерева, які зустрічаються в методичних вказівка і зображені за допомогою дужок використовуючи  nltk.Tree() . Використовувати draw() для побудови графічного зображення дерева.
t=nltk.Tree('(S(NP I)(VP(VP(V shot) (NP(Det an) (N elefant))) (PP((P in) (NP((Det my) (N pajamas)))))))')
print t.draw()
t=nltk.Tree('(S((NP((Det the)(Nom((Adj little)(N bear)))))(VP((VP(V saw)(NP(Det the)(Nom(Adj fine)(Adj fat)(N trout))))(PP(P in)(NP(Det the)(Nom(N brook))))))))')
print t.draw()
t=nltk.Tree('(S((NP(Det the)(N dog))(VP(V saw)(NP((Det a)(N man)(PP(P in)(NP(Det the)(N park))))))))')
print t.draw()
t=nltk.Tree('(S((NP(PropN Chattere))(VP(V said)(S(NP(PropN Buster))(VP(V thought)(S((NP((Det the)(N tree)))(VP(V was)(Adj tall)))))))))')
print t.draw()
t=nltk.Tree('(S((NP(Det the)(Nom((Adj angry)(Nom(N bear)))))(VP(V chased)(NP((Det the)(Nom((Adj little)(N squirrell))))))))')
print t.draw()
t=nltk.Tree('(S((NP John)(VP(V saw)(NP Mary))))')
print t.draw()


print "task10"
#Здійснити аналіз послідовності слів: Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo. Оскільки,згідно з http://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo це граматично правильне речення, напишіть контексно-вільну граматику на основі дерева наведеного на цій сторінці з Інтернету. Здійсніть нормалізацію слів (lowercase), для моделювання ситуації коли слухач сприймає це речення на слух. Скільки дерев розбору може мати це дерево в такому випадку?
Bufalo_grammar = nltk.parse_cfg("""
S -> NP VP
NP -> NP RC | PN N
VP -> V NP
RC -> NP V
PN -> 'Buffalo'
N -> 'buffalo'
V -> 'buffalo'
""")
sent = "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo".split()
parser = nltk.ChartParser(Bufalo_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
    tree.draw()


print "task12"
#Написати програму порівняння швидкодії всіх аналізаторів, які згадувалися в методичних. Використовувати timeit функцію для визначення часу синтаксичного аналізу одного і того самого речення різними аналізаторами.
import timeit
time = timeit.Timer(setup='from nltk import ChartParser')
print time.timeit()
time = timeit.Timer(setup='from nltk import RecursiveDescentParser ')
print time.timeit()
time = timeit.Timer(setup='from nltk import ShiftReduceParser')
print time.timeit()


print "task13"
#Прочита про  "garden path" речення http://en.wikipedia.org/wiki/Garden_path_sentence.
#Оцінити обчислювальну складність аналізу таких речень в порівнянні з труднощами аналізу таких речень людиною?
#"Garden path sentences" - це граматично правильні речення, які починаються в такий спосіб, що в читач спочатку починає розуміти суть зовсім неправильно;
#Ці речення використовуються в психолінгвістиці. Згідно з існуючою теорією в психолінгвістиці, коли читач читає  "garden path sentences", він починаю вибудовувати собі суть речення, але коли дочитує до кінця, то розумію, що суть тут зовсім інша.
#В певний момент читачеві стає очевидно, що наступне слово чи фраза не може бути вставлено в структуру збудовану до цього часу. 
#Приклади "garden path sentence":
#1) The author wrote the novel was likely to be a best-seller.
#The author composed the novel...
#The author wrote that the novel was likely to be a best-seller.
#Людина скоріше(правильніше), ніж комп’ютер аналізує речення (визначає частини мови, синтаксичні зв’язки  і т.д.)
#Синтаксичний аналізатор, так як і людина визначає як поділити речення , але до одного і того ж речення можливо приписувати різні граматичні структури.
#Наприклад  “He ate the cookies on the couch,” це може означати, що він їсть печиво яке є надивані, або, що він сидить на дивані і їсть печиво.
#Отже, як і людина так і машина може припуститися помилки, хоча людина є набагато більше шансів зрозуміти суть речення правильно.
#"""



