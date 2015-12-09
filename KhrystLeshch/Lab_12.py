# -*- coding: utf-8 -*-

#Написати рекурсивну функцію для перегляду дерева, яка визначає його глибину. Дерево з одного вузла має глибину рівну нулю. (глибина піддерева це максимальна глибина його дітей плюс один)
print "task1"
import nltk
t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
def traverse(t):
    try:
        t.node
    except AttributeError:
           print t,
    else:
           print '(', t.node,
           for child in t:
               traverse(child)
           print ')',
print t.height()


print "task4"
#Розширити граматику grammar2 з попередньої лабораторної роботи правилами які розділяють прийменники як перехідні, неперехідні та такі що вимагають PP доповнення. На основі цих правил побудуйте дерево розбору для речення Lee ran away home, використовуючи аналізатор рекурсивного спуску.
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

print "task5"
#Вибрати декілька (2) загальних дієслова та напишіть програми для вирішення наступних задач:
#Пошук дієслів в корпусіPrepositionalPhraseAttachmentCorpusnltk.corpus.ppattach.
#Пошук всіх випадків вживання  дієслова з двома різними  РР в яких перший іменник, або другий іменник або прийменник залишаються незмінними
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    table[key][entry.attachment].add(entry.verb)

for key in sorted(table):
    if len(table[key]) > 1:
        print key, 'N:', sorted(table[key]['N']), 'V:',
        sorted(table[key]['V'])

        
print "task8"
#Здійснити аналіз корпуса Prepositional Phrase Attachment Corpus та спробувати знайти фактори, які впливають на місце приєднання PP.
import nltk
entries = nltk.corpus.ppattach.attachments('training')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
    key = entry.verb + '-' + entry.prep + '-' + entry.noun1
    table[key][entry.attachment].add(entry.verb)
for key in sorted(table):
    if len(table[key]) > 1:
        print key, 'V:', sorted(table[key]['N']), 'V:',
        sorted(table[key]['V'])	


print "task12"
#Розробити програму обробки дерев корпуса Treebank nltk.corpus.treebank, яка вилучить всі правила з кожного з дерев за допомогою Tree.productions(). Правилами, які зустрічаються тільки один раз можна знехтувати. Правила з однаковими лівими частинами  та подібними правими частинами об’єднати для отримання еквівалентного але більш компактного набору правил.
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0002.mrg')[0]
print t
print t.productions()
