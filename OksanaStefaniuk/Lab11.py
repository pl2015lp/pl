# -*- coding: utf-8 -*-

#Task1
#Здійснити аналіз речення Anna walks or Peter drives and nobody laught.
#Знайти частини речення які охоплюють сполучники and та or.
#Побудувати дерева, які відповідають цим двом інтерпретаціям.

print "\n1)\n"

grammar = nltk.parse_cfg(""" 
S -> NP VP
NP -> VP PP
VP -> N V
N -> "Anna"     
V -> "walks"
PP -> P VP
P -> "or"
VP -> N V
N -> "Peter"
V -> "drives"
VP -> PP VP
PP -> P
P -> "and"
VP -> N  V
N -> "nobody"
V -> "laught"
""")
sent = "Anna walks or Peter drives and nobody laught".split()
rd_parser = nltk.RecursiveDescentParser(grammar)
for tree in rd_parser.nbest_parse(sent):
	print tree
import nltk
grammar1 = nltk.parse_cfg("""
S -> NP VP
NP -> VP PP
VP -> N V
N -> "Anna"     
V -> "walks"
PP -> P VP
P -> "or"
VP -> N V
N -> "Peter"
V -> "drives"
VP -> PP VP
PP -> P
P -> "and"
VP -> N  V
N -> "nobody"
V -> "laught"
""")
sent = "Anna walks or Peter drives and nobody laught".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
    tree.draw()
grammar = nltk.parse_cfg("""
S -> NP VP
NP -> VP PP
VP -> N V
N -> "Anna"     
V -> "walks"
PP -> P VP
P -> "or"
VP -> N V
N -> "Peter"
V -> "drives"
VP -> PP VP
PP -> P
P -> "and"
VP -> N  V
N -> "nobody"
V -> "laught"
""")
sent = "Anna walks or Peter drives and nobody laught".split()
parser = nltk.ChartParser(grammar)
trees = parser.nbest_parse(sent)
for tree in trees:
	tree.draw()

#Task2
#В класі Tree реалізовано різноманітні корисні методи. Переглянути файл допомоги  Tree з документації
#та описати основні з цих методів (import Tree,  help(Tree).

print "\n2)\n"

import nltk
from nltk import Tree
print help(Tree)

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

#Task3
#Перетворити всі дерева , які зустрічаються в методичних вказівка і зображені за допомогою дужок використовуючи  nltk.Tree() .
#Використовувати draw() для побудови графічного зображення дерева.


print "\n4)\n"

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

#Task4
#Написати програму для пошуку відповіді на питання.
#Чи може grammar1 граматика використовуватися для опису речення довжиною більше ніж 20 слів?

print "\n8)\n"

from nltk import ShiftReduceParser
from nltk import parse_cfg
import nltk
grammar1 = parse_cfg(
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

#Task5
#Здійснити аналіз послідовності слів: Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo. Оскільки, згідно з http://en.wikipedia.org/wiki/Buffalo_buffalo_Buffalo_buffalo_buffalo_buffalo_Buffalo_buffalo це граматично правильне речення, напишіть контексно-вільну граматику на основі дерева наведеного на цій сторінці з Інтернету. Здійсніть нормалізацію слів (lowercase), для моделювання ситуації коли слухач сприймає це речення на слух.
#Скільки дерев розбору може мати це дерево в такому випадку?

print "\n10)\n"

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

#Task6
#Написати програму порівняння швидкодії всіх аналізаторів, які згадувалися в методичних.
#Використовувати timeit функцію для визначення часу синтаксичного аналізу одного і того самого речення різними аналізаторами.

print "\n12)\n"

import timeit
time = timeit.Timer(setup='from nltk import ChartParser')
print time.timeit()
time = timeit.Timer(setup='from nltk import RecursiveDescentParser ')
print time.timeit()
time = timeit.Timer(setup='from nltk import ShiftReduceParser')
print time.timeit()





