# -*- coding: utf-8 -*-
print "\n2)\n"
"""
2.	В класі Tree реалізовано різноманітні корисні методи.
Переглянути файл допомоги  Tree з документації та описати
основні з цих методів (import Tree,  help(Tree).
"""
from nltk import Tree
#help(Tree)
# A Tree represents a hierarchical grouping of leaves and subtrees.
#For example, each constituent in a syntax tree is represented by a single
#Tree.
"""
 Methods defined here:
 |  
 |  __add__(self, v)
 |  
 |  __delitem__(self, index)
 |  
 |  __add__(self, v)
 |  
 |  __delitem__(self, index)
 """



print "\n4)\n"
"""
4.	Перетворити всі дерева , які зустрічаються
в методичних вказівка і зображені за допомогою дужок
використовуючи  nltk.Tree() .
Використовувати draw() для побудови графічного зображення дерева.
"""
t = Tree('(S(NP I)(VP(VP(V shot) (NP(Det an) (N elefant))) (PP((P in) (NP((Det my) (N pajamas)))))))')
t.draw()

t2 = Tree('(S((NP((Det the)(Nom((Adj little)(N bear)))))(VP((VP(V saw)(NP(Det the)(Nom(Adj fine)(Adj fat)(N trout))))(PP(P in)(NP(Det the)(Nom(N brook))))))))')
t2.draw()

t3 = Tree('(S((NP(Det the)(N dog))(VP(V saw)(NP((Det a)(N man)(PP(P in)(NP(Det the)(N park))))))))')
t3.draw()
 

t4 = nltk.Tree('(S((NP(PropN Chattere))(VP(V said)(S(NP(PropN Buster))(VP(V thought)(S((NP((Det the)(N tree)))(VP(V was)(Adj tall)))))))))')
t4.draw()
 

t5 = nltk.Tree('(S((NP(Det the)(Nom((Adj angry)(Nom(N bear)))))(VP(V chased)(NP((Det the)(Nom((Adj little)(N squirrell))))))))')
t5.draw()
 

t6 = nltk.Tree('(S((NP John)(VP(V saw)(NP Mary))))')
t6.draw()

print "\n6)\n"

8.	Написати програму для пошуку відповіді на питання.
Чи може grammar1 граматика використовуватися для опису речення довжиною
більше ніж 20 слів?
"""
from nltk import ShiftReduceParser
from nltk import parse_cfg
import nltk

grammar1 = parse_cfg("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | | "Ilona" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with" | "when" 
  """)
#sent = "Mary saw Bob in the telescope when John walked with the dog in the park".split()
sent = "Mary saw Ilona in the park".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.nbest_parse(sent):
      print tree

"""
10.	Здійснити аналіз послідовності слів:
Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo.
Оскільки, згідно з http://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo
це граматично правильне речення, напишіть контексно-вільну граматику на основі дерева наведеного на цій сторінці з Інтернету.
Здійсніть нормалізацію слів (lowercase), для моделювання ситуації коли слухач сприймає це речення на слух. Скільки дерев розбору може мати це дерево в такому випадку? 
"""
Buffalo_grammar = nltk.parse_cfg("""
S -> NP VP
NP -> NP RC | PN N
VP -> V NP
RC -> NP V
PN -> 'Buffalo'
N -> 'buffalo'
V -> 'buffalo'
""")
sent = "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo".split()
parser = nltk.ChartParser(Buffalo_grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
    tree.draw()
sentence="Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"
print sentence.lower()
a=sentence.lower()
b=a.split()
for tree in rd_parser.nbest_parse(b):
	print tree
"""
12.	Написати програму порівняння швидкодії всіх аналізаторів, які згадувалися в методичних.
Використовувати timeit функцію для визначення часу синтаксичного аналізу одного і того самого речення різними аналізаторами.
"""
rd_parser = nltk.RecursiveDescentParser(grammar1)
sr_parser = nltk.ShiftReduceParser(grammar1)
sent1 = "Mary saw Bob".split(
def timeit(sent1,parser):
    import time
    start=time.clock()
    print parser.parse(sent1)
    return time.clock()-start
timeit(sent1,rd_parser)
timeit(sent1,sr_parser)
import timeit
t1 = timeit.Timer(setup='from nltk import RecursiveDescentParser ')
t1.timeit()
t2 = timeit.Timer(setup='from nltk import ShiftReduceParser')
t2.timeit()
"""
"""
13.	Прочитати про  "garden path" речення http://en.wikipedia.org/wiki/Garden_path_sentence.
Оцінити обчислювальну складність аналізу таких речень в порівнянні з труднощами аналізу таких речень людиною?

"Garden path sentences" - це граматично правильні речення, які починаються в такий спосіб, що в читач спочатку починає розуміти суть зовсім неправильно;
Ці речення використовуються в психолінгвістиці. Згідно з існуючою теорією в психолінгвістиці, коли читач читає  "garden path sentences", він починаю вибудовувати
собі суть речення, але коли дочитує до кінця, то розумію, що суть тут зовсім інша.
 В певний момент читачеві стає очевидно, що наступне слово чи фраза не може бути вставлено в структуру збудовану до цього часу. 
Приклади "garden path sentence":
1) The author wrote the novel was likely to be a best-seller.
The author composed the novel...
The author wrote that the novel was likely to be a best-seller.
Людина скоріше(правильніше), ніж комп’ютер аналізує речення (визначає частини мови, синтаксичні зв’язки  і т.д.)
Синтаксичний аналізатор, так як і людина визначає як поділити речення , але до одного і того ж речення можливо приписувати різні граматичні структури.
Наприклад  “He ate the cookies on the couch,” це може означати, що він їсть печиво яке є надивані, або, що він сидить на дивані і їсть печиво.
Отже, як і людина так і машина може припуститися помилки, хоча людина є набагато більше шансів зрозуміти суть речення правильно.
"""

