# -*- coding: utf-8 -*-
# Використовуючи компаративний словник знайти близькі слова для німецької, італійської та англійської мов. Чи можуть отриані результати використовуватися для здійснення перекладу?

from nltk.corpus import swadesh
print swadesh.fileids()
fr2en = swadesh.entries (['de', 'it', 'en'])
print fr2en

# Здійснити аналіз словника вимов. Знайти скільки різних слів він містить. Який відсоток слів з цього словника можуть мати різну вимову?
from nltk.corpus import cmudict
entries=cmudict.entries()
print len(entries)
print entries[:20]
a=[i[0] for i in entries]
print len(set(a))
print(1-123455/133737)*100


# Який відсоток синсетів іенників не мають гіпонімів? До всіх синсетів можна доступитися за допомогою wn.all_synsets('n')
from nltk.corpus import wordnet as wn
s=0
h=0
for w in wn.all_synsets ('n'):
    s=s+1
    if len(w.hyponyms())==0:
        h=h+1

print s
print h
result=(h*100)/s
print result


# Модифікувати рограму генерації випадкового тексту для виконання наступного: тренувати програму на текстах різних жанрів та різних корпусів. Генерацію тексту провести з 5-ма різними початковими словами. Результати проаналізувати та порівняти.
import nltk
from nltk.corpus import*
from nltk import bigrams
from nltk.probability import ConditionalFreqDist
def generate_model (txt, w, num = 20):
    bigram = bigrams(txt)
    cfd=ConditionalFreqDist(bigram)
    for i in range(num):
        print w,
        w=cfd[w].max()
text=genesis.words()
word=raw_input ('input  a word ')
print generate_model(text, word)


# Полісемія - це явище коли одне слово має декілька значень (іменник dog має 7 значень, кількість яких визначити можна як len(wn.synsts('dog', 'n'))). Знайдіть середнє значення полісемії для прикметників.
import nltk
from nltk.corpus import wordnet as wn
n=0
k=0
for synset in wn.all_synsets('a'):
    n=n+len(synset.lemmas)
    k=k+1
print n
print k
print n/k


# Використовуючи один з методів визначення подібності слів побудуйте відсортований по спаданню список значень подібності для наступних пар слів: bird-crane, tool-implement, brother-monk, lad-brother, crane-implement, journey-car, monk-oracle, cemetery-woodland.
import nltk
from nltk.corpus import wordnet as wn
bird=wn.synset('bird.n.01')
crane=wn.synset('crane.n.01')
print crane.path_similarity(bird)

tool=wn.synset('tool.n.01')
implement=wn.synset('implement.n.01')
print implement.path_similarity(tool)

brother=wn.synset('brother.n.01')
monk=wn.synset('monk.n.01')
print monk.path_similarity(brother)

lad=wn.synset('lad.n.01')
brother=wn.synset('brother.n.01')
print brother.path_similarity(lad)

crane=wn.synset('crane.n.01')
implement=wn.synset('implement.n.01')
print implement.path_similarity(crane)

journey=wn.synset('journey.n.01')
car=wn.synset('car.n.01')
print car.path_similarity(journey)

monk=wn.synset('monk.n.01')
oracle=wn.synset('oracle.n.01')
print oracle.path_similarity(monk)

cemetery=wn.synset('cemetery.n.01')
woodland=wn.synset('woodland.n.01')
print woodland.path_similarity(cemetery)

furnace=wn.synset('furnace.n.01')
stove=wn.synset('stove.n.01')
print stove.path_similarity(furnace)

food=wn.synset('food.n.01')
fruit=wn.synset('fruit.n.01')
print fruit.path_similarity(food)

bird=wn.synset('bird.n.01')
cock=wn.synset('cock.n.01')
print cock.path_similarity(bird)

