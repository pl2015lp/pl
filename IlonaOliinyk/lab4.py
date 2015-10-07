# -*- coding: utf-8 -*-
#1.	Дослідити зв’язки голонім-меронім для іменників.
#Знайти іменники для демонстрації наступних зв’язків:
#member_meronyms(), part_meronyms(), substance_meronyms(),
#member_holonyms(), part_holonyms(), та substance_holonyms().
print "\n1)\n"

from nltk.corpus import wordnet as wn
#Меронім — це об'єкт, що є частиною іншого.
#учитель — меронім для школи
a = wn.synset('school.n.01').member_meronyms()
print a
#двигун є частиною автомобіля
b = wn.synset('tree.n.01').part_meronyms()
print b
#чай складається із кофеїну
c = wn.synset('tea.n.01').substance_meronyms()
print c
#холонім це ціле від певної частинки
#дерево складає ліс, ліс - це ціле
d = wn.synset('tree.n.01').member_holonyms()
print d
#око складає обличчя, обличчя - це ціле
f = wn.synset('eye.n.01').part_holonyms()
print f
#сльоза - це ціле, а вода це її складова
ff = wn.synset('water.n.01').substance_holonyms()
print ff


#3.	Побудувати умовний частотний розподіл для корпусу імен.
#Знайти які перші літери частіше використовуються в чоловічих та жіночих іменах.

print "\n3)\n"
import nltk
names = nltk.corpus.names
print names.fileids()
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
          for fileid in names.fileids()
          for name in names.words(fileid))

cfd.tabulate()
cfd.plot()
#згідно з даними графіка жіночі імена найчастіше починаються літерою 'М', а чоловічі – літерою 'S'.

#6.	Визначити функцію supergloss(s) , яка буде приймати синсет s як аргумент
#і повертати стрічку в якій будуть поєднані всі описи всіх значень синсету
# s та описи всіх  гіпернімів та гіпонімів s.

#Гіперонім — слово з ширшим значенням. Гіпонім - слово з вужчим значенням.
#Собака гіперонім до бульдога, а бульдог гіпонім до собаки.
print "\n6)\n"
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

#8.	Модифікувати програму генерації випадкового тексту для виконання наступного:
#тренувати програму на текстах різних жанрів та різних корпусів.
#Генерацію тексту провести з 5-ма різними початковими словами.

from nltk.corpus import brown
brown.categories()
def generate_model(cfdist, word, num=15):
    for i in range(num):
        print word,
        word = cfdist[word].max()
#генерація тексту з корпуса  Brown з жанру news
text1 = nltk.corpus.brown.words(categories='news')
bigrams1 = nltk.bigrams(text1)
cfd = nltk.ConditionalFreqDist(bigrams1)
print "Random text_1from Brown from'news'\n"
generate_model(cfd, 'reading')
#генерація тексту з корпуса  Brown з жанру adventure
print "\nRandom text_2from Brown from'adventure'\n"
text2 = nltk.corpus.brown.words(categories='adventure')
bigrams2 = nltk.bigrams(text2)
cfd = nltk.ConditionalFreqDist(bigrams2)
generate_model(cfd, 'reading')
# Імпортуємо інший корпус текстів Gutenberg
from nltk.corpus import gutenberg
print gutenberg.fileids()
text3 = gutenberg.words('austen-persuasion.txt')
bigrams3 = nltk.bigrams(text3)
cfd = nltk.ConditionalFreqDist(bigrams3)
print "\nRandom text_3from Gutenberg from'austen-persuasion.txt'\n"
generate_model(cfd,'What')

text4 = gutenberg.words('shakespeare-caesar.txt')
bigrams4 = nltk.bigrams(text4)
cfd = nltk.ConditionalFreqDist(bigrams4)
print "\nRandom text_4from Gutenberg from'shakespeare-caesar.txt'\n"
generate_model(cfd,'The')

text5 = gutenberg.words('chesterton-ball.txt')
bigrams5 = nltk.bigrams(text5)
cfd = nltk.ConditionalFreqDist(bigrams5)
print "\nRandom text_5from Gutenberg from'chesterton-ball.txt'\n"
generate_model(cfd,'for')

#10.	Полісемія - це явище коли одне слово має декілька значень
#( іменник dog має 7 значень, кількість яких визначити можна як
#len(wn.synsets('dog', 'n'))).
#Знайдіть середнє значення полісемії для іменників.

noun_meanings = []
for i in wn.all_synsets ('n'):
    #додаємо слова
    for j in i.lemma_names:
        noun_meanings.append (j)

polysemantic_nouns = len(set(noun_meanings))
print 'Number of polysemantic nouns:\t%s'%(polysemantic_nouns)


noun_words = 0
for k in set (noun_meanings):
    noun_words = noun_words + len (wn.synsets (k, 'n'))

print 'Number of nouns:\t%s'%(noun_words)
noun_poly = float(noun_words) / polysemantic_nouns
print'Average polysemy value of nouns:\t%s'%(noun_poly)

#14.	Використовуючи один з методів визначення подібності слів побудуйте
#відсортований по спаданню список значень подібності для наступних пар слів:
#car-automobile, gem-jewel, journey-voyage, boy-lad, coast-shore,
#asylum-madhouse, magician-wizard, midday-noon, furnace-stove, food-fruit, bird-cock.
from nltk.corpus import wordnet as wn
#car - automobile
car = wn.synset('car.n.01')
automobile = wn.synset('automobile.n.01')
a = car.path_similarity(automobile)
print a
#gem-jewel
gem = wn.synset('gem.n.01')
jewel = wn.synset('jewel.n.01')
b = gem.path_similarity(jewel)
print b
#journey - voyage
journey = wn.synset('journey.n.01')
voyage = wn.synset('voyage.n.01')
c = journey.path_similarity(voyage)
print c
#boy - lad
boy = wn.synset('boy.n.01')
lad = wn.synset('lad.n.01')
d = boy.path_similarity(lad)
print d
#coast - shore
coast = wn.synset('coast.n.01')
shore = wn.synset('shore.n.01')
e = coast.path_similarity(shore)
print e
#asylum - madhouse
asylum = wn.synset('asylum.n.01')
madhouse = wn.synset('madhouse.n.01')
f = asylum.path_similarity(madhouse)
print f
#magician - wizard
magician = wn.synset('magician.n.01')
wizard = wn.synset('wizard.n.01')
g = magician.path_similarity(wizard)
print g
#midday - noon
midday = wn.synset('midday.n.01')
noon = wn.synset('noon.n.01')
h = midday.path_similarity(noon)
print h
#furnace - stove
furnace = wn.synset('furnace.n.01')
stove = wn.synset('stove.n.01')
i = furnace.path_similarity(stove)
print i
#food - fruit
food = wn.synset('food.n.01')
fruit = wn.synset('fruit.n.01')
k = food.path_similarity(fruit)
print k
#bird - cock - 
bird = wn.synset('bird.n.01')
cock = wn.synset('cock.n.01')
l = bird.path_similarity(cock)
print l
6
#сортування елементів за спаданням
list = [a,b,c,d,e,f,g,h, i,k,l]
print list

def insertion_sort(arrayToSort):
    a = arrayToSort
    for i in range(len(a)):
        v = a[i]
        j = i;
        while (a[j-1] < v) and (j > 0):
            a[j] = a[j-1]
            j = j - 1
        a[j] = v
    return a


sortedList =  insertion_sort(list)
print sortedList


