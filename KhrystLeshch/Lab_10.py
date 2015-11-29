# -*- coding: utf-8 -*-
print "task1"
#Здійсніть тренування юніграм аналізатора на основі частини корпуса, який відповідає першій або другій літері прізвища студента та виконайте аналіз тексту з частини корпуса, яка відповідає першій або другій літері імені студента. Результати поясніть. Чому для деяких слів не встановлені теги.
import nltk
from nltk.corpus import brown
brown_tagged_sents=brown.tagged_sents(categories='hobbies')
brown_sents=brown.sents(categories='hobbies')
unigram_tagger=nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(brown_sents[40])
print unigram_tagger.evaluate(brown_tagged_sents)
brown_tagged_sents_1=brown.tagged_sents(categories='mystery')
brown_sents_1=brown.sents(categories='mystery')
print unigram_tagger.tag(brown_sents_1[40])
print unigram_tagger.evaluate(brown_tagged_sents_1)
t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(brown_tagged_sents, backoff=t0)
print t1.evaluate(brown_tagged_sents)
print t1.evaluate(brown_tagged_sents_1)


print "task2"
# Прочитати файл допомого про морфологічний аналізатор на основі афіксів(help(nltk.AffixTagger)). Напишіть програму, яка викликає аналізатор на основі афіксів в циклі, з різними значеннями довжини афіксів і мінімальними довжинами слів. При яких значеннях можна отримати кращі результати.
brown_p=nltk.corpus.brown.tagged_sents(categories='mystery')
sent=nltk.corpus.brown.sents(categories='mystery')[289]
afsize=[-1,-2,-3]
stem_size=[2,3]
for i in afsize:
    for j in stem_size:
        tagger=affix_tagger=nltk.AffixTagger(brown_p,affix_length=i,min_stem_length=j)
        analyze=tagger.tag(sent)
        evaluate=tagger.evaluate(brown_p)
        print analyze
        print tagger
        print evaluate

print "task3"
#Здійсніть тренування біграм аналізатора на частинах корпуса з вправи 3.1 без backoff аналізатора. Перевірте його роботу. Що відбулося з продуктивністю аналізатора? Чому?
brown_tags=brown.tagged_sents(categories='adventure')
test=brown.tagged_sents(categories='news')
bigram_tagger=nltk.BigramTagger(brown_tags)
print bigram_tagger.evaluate(test)
t1=nltk.DefaultTagger('NN')
t2=nltk.BigramTagger(brown_tags,backoff=t1)
print t2.evaluate(test)


print "task4"
# Дослідити наступні проблеми. що виникають при роботі з аналізатором на основі підстановок: що відбудеться з продуктивністю аналізатора, якщо опустити backoff аналізатор (дослідити на частині броунівського корпусу, яка відповідає першій або другій літері прізвища студента); на основі рис.1. та відповідного фрагмента програми встановити точку максимальної продуктивності незважаючи на розмір списку (об’єм оперативної пам’яті) і точку достатньої продуктивності при мінімальному розмірі списку.
fd=nltk.FreqDist(brown.words(categories='news'))
most_freq_words=fd.keys()[:100]
c=most_freq_words
print c
cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
likely_tags=dict((word, cfd[word].max()) for word in most_freq_words)
baseline_tagger=nltk.UnigramTagger(model=likely_tags, backoff=nltk.DefaultTagger('NN'))
print baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[1000])

#без backoff
baseline_tagger=nltk.UnigramTagger(model=likely_tags)
print baseline_tagger.tag(nltk.corpus.brown.sents(categories='news')[1000]), 
#Якщо опустити backoff аналізатор, продуктивність аналізатора на основі підстановок зменшиться. Анлізатор не присвоюватиме ніяких тегів словоформам, які не входять до означеного списку начастотніших слів і ставитиме їм у відповідність тег None. При використанні bsckoff аналізатора таким словам присвоюється тег NN, що збільшує ефективність аналізатора.
def performance (cfd, wordlist):
    It=dict((word, cfd[word].max())for word in wordlist)
    baseline_tagger=nltk.UnigramTagger(model=It, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))
def display():
    import pylab
    words_by_freq=list(nltk.FreqDist(brown.words(categories='news')))
    cfd=nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes=2** pylab.arange(15)
    perfs=[performance(cfd, words_by_freq[:size]) for  size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
    
                        
print "task5"
# Знайдіть розмічені корпуси текстів для інших мов які вивчаєте або володієте(українська, польська, німецька, російська, італійська, японська). Здійсніть тренування та оцініть продуктивність роботи різних аналізаторів та комбінацій різних аналізаторів. Точність роботи аналізаторів порівняйте з точністю роботи аналізаторів для англійських корпусів. Результати поясніть.

import nltk, re, pprint
from nltk.corpus import*
size=int(len(mac_morpho.tagged_sents())*0.9)
print size
train=mac_morpho.tagged_sents()[:size]
test=mac_morpho.tagged_sents()[size:]
u_t=nltk.UnigramTagger(train)
print u_t.evaluate(test)
b_t=nltk.BigramTagger(train)
print b_t.evaluate(test)
y_t=nltk.TrigramTagger
t_t=nltk.TrigramTagger(train)
print t_t.evaluate(test)
t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(train,backoff=t0)
t2=nltk.BigramTagger(train,backoff=t1)
t3=nltk.TrigramTagger(train,backoff=t2)
print t3.evaluate(test)

print "task6"
#Створити аналізатор по замовчуванню та набір юніграм і n-грам аналізаторів. Використовуючи backoff здійсніть тренування аналізаторів на частині корпуса з вправи 3.2. Дослідіть три різні комбінації поєднання цих аналізаторів. Перевірте точність роботи аналізаторів. Визначіть комбінацію аналізаторів з максимальною точністю аналізу. Змініть розмір даних на яких проводилось тренування. Повторіть експерименти для змінених даних для тренування. Результати порівняйти і пояснити.
default_tagger=nltk.DefaultTagger('NN')
brown_a=nltk.corpus.brown.tagged_sents(categories='belles_lettres')
unigram_tagger=nltk.UnigramTagger(brown_p)
bigram_tagger=nltk.BigramTagger(brown_b, cutoff=0)
t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(brown_b,backoff=t0)
t2=nltk.BigramTagger(brown_b,backoff=t1)
print nltk.tag.accuracy(t2,brown_b)
brown_a=nltk.corpus.brown.tagged_sents(categories='adventure')
print nltk.tag.accuracy(t2, brown_a)
to=nltk.UnigramTagger(brown_b)
t1=nltk.BigramTagger(brown_b, backoff=t0)
t2=nltk.DefaultTagger('NN')
print nltk.tag.accuracy(t2, brown_a)
to=nltk.DefaultTagger('NN')
t1=nltk.BigramTagger(brown_b, backoff=t0)
t2=nltk.UnigramTagger(brown_b,backoff=t2)
print nltk.tag.accuracy(t2, brown_a)
to=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(brown_a, backoff=t0)
t2=nltk.BigramTagger(brown_a,backoff=t1)
print nltk.tag.accuracy(t2, brown_a)
to=nltk.DefaultTagger('NN')
unigram_tagger=nltk.UnigramTagger(brown_b)
unigram_tagger=nltk.UnigramTagger(brown_a)
brown_n=nltk.corpus.brown.tagged_sents(categories='news')
brown_r=nltk.corpus.brown.tagged_sents(categories='romance')
to=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(brown_n, backoff=t0)
t2=nltk.BigramTagger(brown_n,backoff=t1)
print nltk.tag.accuracy(t2, brown_a)
to=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(brown_r, backoff=t0)
t2=nltk.BigramTagger(brown_r,backoff=t1)
print nltk.tag.accuracy(t2, brown_a)
to=nltk.DefaultTagger('NN')
t1=nltk.BigramTagger(brown_r, backoff=t0)
t2=nltk.UnigramTagger(brown_r,backoff=t1)
print nltk.tag.accuracy(t2, brown_a)
# я здійснила тренування створених аналізаторів на частині корпусу "'belles lettres'"  і дослідила три різні комбінації поєднання цих аналізаторів. Також я перевірила точність їх роботи на частині корпусу "adventure". Найефективнішою виявилась комбінація з першим аналізатором по замочванню, другим - юніграм аналізатором і третім - біграм аналізатором. Ефективність комбінації аналізаторів з перестановкою юніграм і біграм аналізаторів не дуже сильно відрізнялась від максимальої. Потім я змінила частину корпуса, на якому тренувала аналізатори("news" i "romance") і повторила експерименти. Точність аналізаторів зменшилась, але найефективнішою залишилась та сама комбінація аналізаторів.

print "task7"
# Прочитати стрічку документування функції demo Brill аналізатора. Здійснити експерименти з різними значення параметрів цієї функції. Встановити який взаємозв’язок є між часом тренування (навчання аналізатора) і точністю його роботи.
from nltk.book import*
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.80000000000000004, trace=3)
print 'Result: Training unigram tagger: [accuracy: 0.832151], Training bigram tagger: [accuracy: 0.837930], Training Brill tagger on 1600 sentences... Found 9757 useful rules.'

