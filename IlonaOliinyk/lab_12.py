# -*- coding: utf-8 -*-
"""
1.	Написати рекурсивну функцію для перегляду дерева, яка визначає його глибину.
Дерево з одного вузла має глибину рівну нулю.
(глибина піддерева це максимальна глибина його дітей плюс один)
"""
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
#4


"""
4.	Розширити граматику grammar2 з попередньої лабораторної роботи
правилами які розділяють прийменники як перехідні, неперехідні та такі що вимагають PP доповнення.
На основі цих правил побудуйте дерево розбору для речення Lee ran away home,
використовуючи аналізатор рекурсивного спуску.
"""
from nltk import RecursiveDescentParser
from nltk import parse_cfg
import nltk
grammar2 = nltk.parse_cfg("""
S  -> NP VP
NP -> Det Nom | PropN | N
TP -> PRO NP  
IP -> PRO ADJ | PRO | PRO ADV | NP PRO NP
PC -> PRO PP
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log' | 'Lee' | 'home'
Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
V -> 'ran' | 'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put' | 'give' | 'lead'
P -> 'on' | 'away' | 'up with'| 'up'
""")
sent = "Lee ran away home".split()
rd_parser = RecursiveDescentParser(grammar2)
for tree in rd_parser.nbest_parse(sent):
    print tree
#(S (NP (N Lee)) (VP (V ran) (PP (P away) (NP (N home)))))
"""
5.	Вибрати декілька (2) загальних дієслова та напишіть програми для вирішення наступних задач:
Пошук дієслів в корпусі Prepositional Phrase Attachment Corpus nltk.corpus.ppattach.
Пошук всіх випадків вживання  дієслова з двома різними  РР в яких перший іменник,
або другий іменник або прийменник залишаються незмінними
Розробити правила CFG граматики  для врахування цих випадків.
 """
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    table[key][entry.attachment].add(entry.verb)

	
for key in sorted(table):
    if len(table[key]) > 1:
	    print key, 'N:', sorted(table[key]['N']), 'V:',
	    sorted(table[key]['V'])

"""
%-below-level N: ['left'] V:
['be']
%-from-year N: ['was'] V:
['declined', 'dropped', 'fell', 'grew', 'increased', 'plunged', 'rose', 'was']
%-in-August N: ['was'] V:
['climbed', 'fell', 'leaping', 'rising', 'rose']
%-in-September N: ['increased'] V:
['climbed', 'declined', 'dropped', 'edged', 'fell', 'grew', 'plunged', 'rose', 'slipped']
%-in-week N: ['declined'] V:
['was']
%-to-% N: ['add', 'added', 'backed', 'be', 'cut', 'go', 'grow', 'increased', 'increasing', 'is', 'offer', 'plummet', 'reduce', 'rejected', 'rise', 'risen', 'shaved', 'wants', 'yield', 'zapping'] V:
['fell', 'rise', 'slipped']
"""

"""
7.	Використовуючи позиції в дереві побудувати список підметів перших
100 речень корпусу Penn treebank; для спрощення представлення
результатів підмети представляти як піддерева з глибиною не більше 2..
"""
from nltk.corpus import treebank
treebank.train = treebank.parsed_sents()[:100]
def filter(tree):
    child_nodes = [child.node for child in tree
                   if isinstance (child, nltk.Tree) and len(tree) <2]
    return tree.node == 'NP-SBJ'
[subtree for tree in treebank.train for subtree in tree.subtrees(filter)]

"""
12.Розробити програму обробки дерев корпуса Treebank
nltk.corpus.treebank , яка вилучить всі правила з кожного з дерев
за допомогою  Tree.productions(). Правилами, які зустрічаються тільки
один раз можна знехтувати. Правила з однаковими лівими частинами  та
подібними правими частинами
об’єднати для отримання еквівалентного але більш компактного набору правил.
"""
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0002.mrg')
print t
"""
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
  """
t.productions()

      

		
