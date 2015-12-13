# -*- coding: utf-8 -*-

#Task1
#Написати рекурсивну функцію для перегляду дерева, яка визначає його глибину.
#Дерево з одного вузла має глибину рівну нулю.
#(глибина піддерева це максимальна глибина його дітей плюс один)


print "\n1)\n"

from nltk import Tree
tree = Tree('(S (NP Mother) (VP brought (NP the candy)))')
def traverse(tree):
	try:
		tree.node
	except AttributeError:
		print tree,
	else:
		print '(', tree.node,
		for child in tree:
			traverse (child)
		print ')'
	        
print tree.height()

#Task2
#chart parser додає але ніколи не видаляє дуги з  chart. Чому?


print "\n3)\n"

print 'Since it is a dynamic programming and it remembers only imtermediary result'

#Task3
#Вибрати декілька (2) загальних дієслова та напишіть програми для вирішення наступних задач:
#Пошук дієслів в корпусі Prepositional Phrase Attachment Corpus nltk.corpus.ppattach. Пошук всіх випадків вживання  дієслова з двома різними
#РР в яких перший іменник, або другий іменник або прийменник залишаються незмінними
#Розробити правила CFG граматики  для врахування цих випадків.

print "\n5)\n"

entries = nltk.corpus.ppattach.attachments('training')
table=nltk.defaultdict(lambda:nltk.defaultdict(set))
for entry in entries:
	key=entry.noun1 + '-' + entry.prep + '-' + entry.noun2
	table[key][entry.attachment].add(entry.verb)
for key in sorted(table):
	if len(table[key])>1:
		print key, 'N', sorted(table[key]['N']),'V:', sorted(table[key]['V'])

#Task4
#Використовуючи позиції в дереві побудувати список підметів перших
#100 речень корпусу Penn treebank; для спрощення представлення
#результатів підмети представляти як піддерева з глибиною не більше 2

print "\n7)\n"

from nltk.corpus import treebank
treebank.train = treebank.parsed_sents()[:100]
def filter(tree):
    child_nodes = [child.node for child in tree
                   if isinstance (child, nltk.Tree) and len(tree) <2]
    return tree.node == 'NP-SBJ'
[subtree for tree in treebank.train for subtree in tree.subtrees(filter)]


#Task5
#Розробити програму обробки дерев корпуса Treebank  nltk.corpus.treebank , яка вилучить всі правила з кожного з дерев за допомогою  Tree.productions().
#Правилами, які зустрічаються тільки один раз можна знехтувати. Правила з однаковими лівими частинами
#та подібними правими частинами об’єднати для отримання еквівалентного але більш компактного набору правил.


print "\n15)\n"

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0002.mrg')

(S
  (NP-SBJ-1
    (NP (NNP Rudolph) (NNP Agnew))
    (, ,)
    (UCP
      (ADJP (NP (CD 55) (NNS years)) (JJ old))
      (CC and)
      (NP
        (NP (JJ former) (NN chairman))
        (PP
          (IN of)
          (NP (NNP Consolidated) (NNP Gold) (NNP Fields) (NNP PLC)))))
    (, ,))
  (VP
    (VBD was)
    (VP
      (VBN named)
      (S
        (NP-SBJ (-NONE- *-1))
        (NP-PRD
          (NP (DT a) (JJ nonexecutive) (NN director))
          (PP
            (IN of)
            (NP
              (DT this)
              (JJ British)
              (JJ industrial)
              (NN conglomerate)))))))
  (. .))

print t.productions()



