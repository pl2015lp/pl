# -*- coding: utf8 -*-
import nltk
from nltk.book import *
#Task2
#Використовуючи компаративний словник знайти близькі слова для німецької, італійської та англійської мов.
#Чи можуть отримані результати використовуватися для здійснення перекладу?
print "\n1)\n"
from nltk.corpus import swadesh
swadesh.fileids()
de2it2en=swadesh.entries(['de','it','en'])
print de2it2en

#Task5
#Який відсоток синсетів іменників не мають гіпонімів?
#До всіх синсетів можна доступитися за допомогою wn.all_synsets('n').
print "\n2)\n"
noun = list(wn.all_synsets('n'))
len(noun)
noun_without_hyponyms = [n for n in wn.all_synsets('n') if not n.hyponyms()]
len(noun_without_hyponyms)
result = float(len(noun_without_hyponims))/float(len(noun))*100
result

#Task6
#Визначити функцію supergloss(s),яка буде приймати синсет s як аргумент
#і повертати стрічку в якій будуть поєднані всі описи всіх значень синсету s та описи всіх  гіпернімів та гіпонімів s.
print "\n3)\n"
wn = nltk.corpus.wordnet
import string
#strig1 = string.join(list1)
def supergloss (s):
    srt1 = ">> Definition\n"
    str1 += wn.synset(s).definition + "\n\n>> Hypernyms\n"
    str1 += string.join([word.definition for word in wn.synset(s).hypernyms()]) + "\n\n>> Hyponyms\n"
    str1 += string.join([word.definition for word in wn.synset(s).hyponyms()]) + "\n"
    return str1
result = supergloss('coffee.n.01')
print result

#Task8
#Модифікувати програму генерації випадкового тексту для виконання наступного: тренувати програму на текстах різних жанрів та різних корпусів.
#Генерацію тексту провести з 5-ма різними початковими словами. Результати проаналізувати та порівняти.
print "\n4)\n"
from nltk.corpus import brown
print brown.categories()
brown.words(categories='adventure')
def generate_model(cfdist, word, num=20):
	for i in range(num):
		print word,
		word = cfdist[word].max()
text=brown.words(categories='adventure')
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)
print cfd['The']
print 'First random text'
print generate_model(cfd, 'The')
text1=brown.words(categories='belles_lettres')
bigrams1 = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams1)
print cfd['There']
print 'Second random text'
print generate_model(cfd, 'There')
text2=brown.words(categories='editorial')
bigrams2 = nltk.bigrams(text1)
cfd = nltk.ConditionalFreqDist(bigrams2)
print cfd['This']
print 'Third random text'
print generate_model(cfd, 'This')
from nltk.corpus import gutenberg
print gutenberg.fileids()
text3=gutenberg.words('austen-emma.txt')
bigrams3 = nltk.bigrams(text3)
cfd = nltk.ConditionalFreqDist(bigrams3)
print cfd['Emma']
print 'Fourth random text'
print generate_model(cfd, 'Emma')
text4=gutenberg.words('austen-persuasion.txt')
bigrams4 = nltk.bigrams(text4)
cfd = nltk.ConditionalFreqDist(bigrams4)
print cfd['How']
print 'Fifth random text'
print generate_model(cfd, 'How')

#Task11
#Полісемія - це явище коли одне слово має декілька значень ( іменник dog має 7 значень, кількість яких визначити можна як len(wn.synsets('dog', 'n'))).
#Знайдіть середнє значення полісемії для прикметників.
from nltk.corpus import wordnet as wn
d=[]
for i in wn.all_synsets ('a'):
    for j in i.lemma_names:
        d.append(j)
len (set(d))
print len (set(d))
q=0
for i in set (d):
    q=q+len(wn.synsets(i,'a'))
print q
poly_a=q/len(set(d))
print poly_a
print "\n5)\n"

#Task15
#15Використовуючи один з методів визначення подібності слів побудуйте відсортований по спаданню список значень подібності для наступних пар слів:
#bird-crane, tool-implement, brother-monk, lad-brother, crane-implement,journey-car, monk-oracle, cemetery-woodland.
from nltk.corpus import wordnet as wn
#bird - crane
bird = wn.synset('bird.n.01')
crane = wn.synset('crane.n.01')
a = bird.path_similarity(crane)
print a
#tool-implement
tool = wn.synset('tool.n.01')
implement = wn.synset('implement.n.01')
b = tool.path_similarity(implement)
print b
#brother - monk
brother = wn.synset('brother.n.01')
monk = wn.synset('monk.n.01')
c = brother.path_similarity(monk)
print c
#lad - brother
lad = wn.synset('lad.n.01')
brother = wn.synset('brother.n.01')
d = lad.path_similarity(brother)
print d
#crane - implement
crane = wn.synset('crane.n.01')
implement = wn.synset('implement.n.01')
e = crane.path_similarity(implement)
print e
#journey - car
journey = wn.synset('journey.n.01')
car = wn.synset('car.n.01')
f = journey.path_similarity(car)
print f
#monk - oracle
monk = wn.synset('monk.n.01')
oracle = wn.synset('oracle.n.01')
g = monk.path_similarity(oracle)
print g
#cemetery-woodland
cementery = wn.synset('cementery.n.01')
woodland = wn.synset('woodland.n.01')
h = cementery.path_similarity(woodland)
#сортування елементів за спаданням
s=[]
s.append(a)
s.append(b)
s.append(c)
s.append(d)
s.append(e)
s.append(f)
s.append(g)
s.append(h)
print s
s.sort()
print 'sortyvannia po zrostanniu'
print s
s.reverse()
print 'sortovane po spadanniu'
print s
