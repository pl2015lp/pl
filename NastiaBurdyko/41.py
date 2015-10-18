#1.	Дослідити зв’язки голонім-меронім для іменників. Знайти іменники для демонстрації наступних зв’язків: member_meronyms(*), part_meronyms(*), substance_meronyms(*), member_holonyms(*), part_holonyms(), та substance_holonyms(*).
Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from nltk.corpus import wordnet as wn
>>> wn.synset('building.n.01').part_meronyms()
[Synset('corner.n.03'), Synset('window.n.01'), Synset('cullis.n.01'), Synset('shaft.n.08'), Synset('heating_system.n.01'), Synset('court.n.10'), Synset('floor.n.02'), Synset('interior_door.n.01'), Synset('room.n.01'), Synset('crawlspace.n.01'), Synset('anteroom.n.01'), Synset('exterior_door.n.01'), Synset('skeleton.n.04'), Synset('upstairs.n.01'), Synset('corner.n.11'), Synset('wall.n.01'), Synset('stairway.n.01'), Synset('elevator.n.01'), Synset('annex.n.01'), Synset('roof.n.01'), Synset('cornerstone.n.02'), Synset('cornerstone.n.03'), Synset('foundation_stone.n.01'), Synset('scantling.n.01')]
>>> wn.synset('government.n.01').member_meronyms()
[Synset('government_department.n.01'), Synset('government_officials.n.01'), Synset('division.n.04'), Synset('judiciary.n.01'), Synset('legislature.n.01'), Synset('executive.n.02')]
>>> wn.synset('tree.n.01').member_holonyms()
[Synset('forest.n.01')]
>>> wn.synset('water.n.01').substance_holonyms()
[Synset('tear.n.01'), Synset('perspiration.n.01'), Synset('snowflake.n.01'), Synset('ice_crystal.n.01'), Synset('ice.n.01'), Synset('body_of_water.n.01')]
>>> wn.synset('water.n.01').substance_meronyms()
[Synset('oxygen.n.01'), Synset('hydrogen.n.01')]
>>> wn.synset('room.n.01').part_holonyms()
[Synset('building.n.01')]

#3.	Побудувати умовний частотний розподіл для корпусу імен. Знайти які перші літери частіше використовуються в чоловічих та жіночих іменах.
import nltk
from nltk.corpus import brown
names = nltk.corpus.names
names.fileids()
male_names = names.words('male.txt')
female_names = names.words('female.txt')

cfd = nltk.ConditionalFreqDist(
  (fileid, name[0])
  for fileid in names.fileids()
 for name in names.words(fileid))
cfd.plot()
#Жіночі імена найчастіше почиаються на букви C,M,S а чоловічі на M,S,W.

#4.	Здійснити аналіз словника вимов. Знайти скільки різних слів він містить. Який відсоток слів з цього словника можуть мати різну вимову?

import nltk
from nltk.corpus import cmudict
entries = nltk.corpus.cmudict.entries()
len(entries)
>>> len(entries)
133737

def vymova():
  import nltk
  from nltk.corpus import cmudict
  entries = cmudict.entries()
  words = map(lambda (word, pron) : word, entries)
  distinct_words = set(words)
  fd = nltk.FreqDist(words)
  multi_prons = 0
  for key in fd.keys():
    if fd[key] == 1:
      break
    multi_prons = multi_prons + 1
  print "#-одна вимова:", len(distinct_words)
  print "#-кілька вимов:", multi_prons
  >>> vymova()
#-одна вимова: 123455
#-кілька вимов: 9241
>>> from __future__ import division
>>> 9241*100/123455
7.485318537118788
>>>


#7.	Модифікувати програму генерації випадкового тексту для виконання наступного: зберігати можливі наступні слова у списку та вибирати їх за допомогою random.choice() попередньо виконавши import random.


>>> import nltk
>>> from nltk.corpus import genesis
>>> import random
>>> def generate_model(cfdist,word,num=15):
	m_list = []
	for i in range(num):
		m_list.append(word)
		word=random.choice(cfdist[word].keys())
		return m_list
	
>>> text=nltk.corpus.genesis.words('german.txt')
>>> bigrams = nltk.bigrams(text)
>>> cfd=nltk.ConditionalFreqDist(bigrams)
>>> print cfd ['lebendig']
<FreqDist: u'.': 1>
>>> print cfd ['Frau']
<FreqDist: u',': 23, u'.': 16, u'und': 10, u'Esaus': 8, u'nehmest': 3, u':': 2, u'hie': 2, u'nahm': 2, u'nehmen': 2, u'von': 2, ...>
>>> 
#10.	Полісемія - це явище коли одне слово має декілька значень ( іменник dog має 7 значень, кількість яких визначити можна як len(wn.synsets('dog', 'n'))). Знайдіть середнє значення полісемії для іменників.

>>> import nltk
>>> from nltk.corpus import wordnet as wn
>>> n=0
>>> k=0
>>> for synset in wn.all_synsets('n'):
	n=n+len(synset.lemmas)
	k=k+1

	
>>> n
146347
>>> k
82115
>>> from __future__ import division
>>> n/k
1.782220057236802

#1.	Використовуючи один з методів визначення подібності слів побудуйте відсортований по спаданню список значень подібності для наступних пар слів: car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore, asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock.
>>> import nltk
>>> from nltk.corpus import wordnet as wn
>>> car=wn.synset('car.n.01')
>>> automobile=wn.synset('automobile.n.01')
>>> automobile.path_similarity(car)
1.0
>>> gem=wn.synset('gem.n.01')
>>> jewel=wn.synset('jewel.n.01')
>>> jewel.path_similarity(gem)
0.125
>>> journey=wn.synset('journey.n.01')
>>> voyage=wn.synset('voyage.n.01')
>>> voyage.path_similarity(journey)
0.25
>>> boy=wn.synset('boy.n.01')
>>> lad=wn.synset('lad.n.01')
>>> lad.path_similarity(boy)
0.3333333333333333
>>> coast=wn.synset('coast.n.01')
>>> shore=wn.synset('shore.n.01')
>>> shore.path_similarity(coast)
0.5
>>> asylum=wn.synset('asylum.n.01')
>>> madhouse=wn.synset('madhouse.n.01')
>>> madhouse.path_similarity(asylum)
0.125
>>> magician=wn.synset('magician.n.01')
>>> wizard=wn.synset('wizard.n.01')
>>> wizard.path_similarity(magician)
0.16666666666666666
>>> midday=wn.synset('midday.n.01')
>>> noon=wn.synset('noon.n.01')
>>> noon.path_similarity(midday)
1.0
>>> furnace=wn.synset('furnace.n.01')
>>> stove=wn.synset('stove.n.01')
>>> stove.path_similarity(furnace)
0.07692307692307693
>>> food=wn.synset('food.n.01')
>>> fruit=wn.synset('fruit.n.01')
>>> fruit.path_similarity(food)
0.09090909090909091
>>> bird=wn.synset('bird.n.01')
>>> cock=wn.synset('cock.n.01')
>>> cock.path_similarity(bird)
0.0625
>>> 