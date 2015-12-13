"""1. Написати рекурсивну функцію для перегляду дерева, яка визначає його глибину. Дерево з одного вузла має глибину рівну нулю. (глибина піддерева це максимальна глибина його дітей плюс один)"""
import nltk
from nltk.corpus import treebank
from nltk import RecursiveDescentParser
from nltk import parse_cfg

def depth(node):
    left_depth = depth(node[0]) if len(node) > 0 and type(node[0]) == nltk.tree.Tree else 1
    right_depth = depth(node[1]) if len(node) > 1 and type(node[1]) == nltk.tree.Tree else 1
    return max(left_depth, right_depth) + 1

tree = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
print 'depth=', depth(tree)
print tree.height()
tree.draw()

"""4. Розширити граматику grammar2 з попередньої лабораторної роботи правилами які розділяють прийменники як перехідні, неперехідні та такі що вимагають PP доповнення. На основі цих правил побудуйте дерево розбору для речення Lee ran away home, використовуючи аналізатор рекурсивного спуску."""
from nltk import RecursiveDescentParser
from nltk import parse_cfg
grammar2 = nltk.parse_cfg("""
S  -> NP VP
NP -> PropN
VP -> Verb NP
NP -> Prep N
Prep -> IT
PropN -> 'Lee'
Verb -> 'ran'
IT -> 'away'
N -> 'home'
""")
sent = 'Lee ran away home'.split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.nbest_parse(sent):
    print tree

"""5. Вибрати декілька (2) загальних дієслова та напишіть програми для вирішення наступних задач:
Пошук дієслів в корпусі Prepositional Phrase Attachment Corpus nltk.corpus.ppattach. Пошук всіх випадків вживання дієслова з двома різними РР в яких перший іменник, або другий іменник або прийменник залишаються незмінними"""
from nltk.corpus import ppattach
print ppattach.fileids()
print ppattach.raw('test')[:100]
entries = nltk.corpus.ppattach.attachments('test')
table = nltk.defaultdict(lambda: nltk.defaultdict(set))
for entry in entries:
    key = entry.verb + '_' + entry.noun1 + '_' + (entry.noun2 or entry.prep)
    table[key][entry.attachment].add(entry.verb)
for key in sorted(table):
    if len(table[key]) > 1:
        print (key, 'V:', sorted(table[key]['V']))[:100]

"""12.Розробити програму обробки дерев корпуса Treebank  nltk.corpus.treebank , яка вилучить всі правила з кожного з дерев за допомогою  Tree.productions(). Правилами, які зустрічаються тільки один раз можна знехтувати. Правила з однаковими лівими частинами  та подібними правими частинами об’єднати для отримання еквівалентного але більш компактного набору правил."""
from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0002.mrg')[0]
print t
print t.productions()





