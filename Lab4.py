"""1.Дослідити зв’язки голонім-меронім для іменників. Знайти іменники для демонстрації наступних зв’язків: member_meronyms(), part_meronyms(), substanc"""
import nltk
from nltk.corpus import wordnet as wn
wn.synset('forest.n.01').member_meronyms()
wn.synset('house.n.01').part_meronyms()
wn.synset('tea.n.01').substance_meronyms()
wn.synset('student.n.01').member_holonyms()
wn.synset('hand.n.01').part_holonyms()
wn.synset('water.n.01').substance_holonyms()

"""5.Який відсоток синсетів іменників не мають гіпонімів? До всіх синсетів можна доступитися за допомогою wn.all_synsets('n')."""
noun = list(wn.all_synsets('n'))
len(noun)
noun_without_hyponyms = [n for n in wn.all_synsets('n') if not n.hyponyms()]
len(noun_without_hyponyms)
result = float(len(noun_without_hyponims))/float(len(noun))*100
result

"""4.Здійснити аналіз словника вимов. Знайти скільки різних слів він містить. Який відсоток слів з цього словника можуть мати різну вимову?"""
entries = nltk.corpus.cmudict.entries()
unique_entries = set([word for word, pron in entries])
len(unique_entries)

convert_entries = {}
entries = nltk.corpus.cmudict.entries()
for word, pron in entries:
    if word not in convert_entries.keys():
        convert_entries[word] = [pron]
    else:
        convert_entries[word].append(pron)

non_unique_count = 0
for key in convert_entries.keys():
    if len(convert_entries[key]) > 1:
        non_unique_count += len(convert_entries[key])

print float(non_unique_count)/float(len(entries)) * 100  

"""9.Модифікувати програму генерації випадкового тексту для виконання наступного: тренування програми на текстах двох різних жанрів та генерації тексту об’єднаного жанру."""
import nltk
from nltk.corpus import state_union
state_union.fileids()
from nltk.corpus import brown
brown.fileids()

def generate_model(cfdist, word, num=15):
	for i in range(num):
		print word,
		word = cfdist[word].max()

text1 = nltk.corpus.state_union.words('1946-Truman.txt')
bigrams1 = nltk.bigrams(text1)
cfd1 = nltk.ConditionalFreqDist(bigrams1)
print cfd1['more']
generate_model(cfd1, 'more')

text2 = nltk.corpus.brown.words('cp14')
bigrams2 = nltk.bigrams(text2)
cfd2 = nltk.ConditionalFreqDist(bigrams2)
print cfd2['more']
generate_model(cfd2, 'more')

text3 = text1+text2
bigrams3 = nltk.bigrams(text3)
cfd3 = nltk.ConditionalFreqDist(bigrams3)
print cfd3['more']
generate_model(cfd3, 'more')

"""12.Полісемія - це явище коли одне слово має декілька значень (іменник dog має 7 значень, кількість яких визначити можна як len(wn.synsets('dog', 'n'))). Знайдіть середнє значення полісемії для дієслів."""
verb = []
for i in wn.all_synsets('v'):
	for j in i.lemma_names:
		verb.append(j)


len(set(verb))
mean_amount = 0
for i in set(verb):
	mean_amount = mean_amount + len(wn.synsets(i,'v'))

mean_amount

poly_verb=float(mean_amount)/float(len(set(verb)))
poly_verb

"""16.Використовуючи один з методів визначення подібності слів побудуйте відсортований по спаданню список значень подібності для наступних пар слів: monk-oracle, cemetery-woodland, food-rooster, coast-hill, forest-graveyard, shore-woodland, monk-slave, coast-forest, lad-wizard, chord-smile, glass-magician, rooster-voyage, noon-string."""
import nltk
from nltk.corpus import wordnet as wn

list_cort = [('monk','oracle'), ('cemetery','woodland'), ('food','rooster',),('coast','hill'), ('forest','graveyard'), ('shore','woodland'),
             ('monk','slave'),('coast','forest'),('lad','wizard'), ('chord','smile'), ('glass','magician'),('rooster','voyage'), ('noon','string')]
result_list=[]
for i,j in list_cort:
    first_word=wn.synsets(i)
    second_word=wn.synsets(j)
    for a in first_word:
        result_list.append('Znachenya pod dlya:') 
        result_list.append(a)
        for b in second_word:
            result_list.append('ta:')
            result_list.append(b)
            result_list.append(a.path_similarity(b))