﻿"""3.1. Здійсніть тренування юніграм аналізатора на основі частини корпуса, який відповідає першій або другій літері прізвища студента та виконайте аналіз тексту з частини корпуса, яка відповідає першій або другій літері імені студента. Результати поясніть. Чому для деяких слів не встановлені теги."""
import nltk
from nltk.corpus import brown
print brown.categories()
brown_tagged_sents = brown.tagged_sents(categories='science_fiction')
brown_sents = brown.sents(categories='science_fiction')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
print unigram_tagger.tag(brown_sents[500])
print unigram_tagger.evaluate(brown_tagged_sents)

brown_tagged_sents1 = brown.tagged_sents(categories='learned')
brown_sents1 = brown.sents(categories='learned')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents1)
print unigram_tagger.tag(brown_sents1[500])
print unigram_tagger.evaluate(brown_tagged_sents1)

"""3.2. Прочитати файл допомого про морфологічний аналізатор на основі афіксів (help(nltk.AffixTagger)). Напишіть програму, яка викликає аналізатор на основі афіксів в циклі, з різними значеннями довжини афіксів і мінімальними довжинами слів. При яких значеннях можна отримати кращі результати."""
help(nltk.AffixTagger)
brown_corp=nltk.corpus.brown.tagged_sents(categories='science_fiction')
sentences=nltk.corpus.brown.sents(categories='science_fiction')[500]
afflength=[-3,-2,-1]
stemlength=[2,3]
for aff in afflength:
    for stem in stemlength:
        tagger=affix_tagger=nltk.AffixTagger(brown_corp,affix_length=aff,min_stem_length=stem)
        analyze=tagger.tag(sentences)
        evaluate=tagger.evaluate(brown_corp)
        print analyze
        print tagger
        print evaluate"""
"""3.3. Здійсніть тренування біграм аналізатора на частинах корпуса з вправи 3.1 без backoff аналізатора. Перевірте його роботу. Що відбулося з продуктивністю аналізатора? Чому?"""
"""brown_tagged_sents = brown.tagged_sents(categories='science_fiction')
brown_sents = brown.sents(categories='science_fiction')
bigram_tagger = nltk.BigramTagger(brown_tagged_sents)
print bigram_tagger.tag(brown_sents[500])
print bigram_tagger.evaluate(brown_tagged_sents)

"""3.4. Дослідити наступні проблеми. що виникають при роботі з аналізатором на основі підстановок: що відбудеться з продуктивністю аналізатора, якщо опустити backoff аналізатор (дослідити на частині броунівського корпусу, яка відповідає першій або другій літері прізвища студента); на основі рис.1. та відповідного фрагмента програми встановити точку максимальної продуктивності незважаючи на розмір списку (об’єм оперативної пам’яті) і точку достатньої продуктивності при мінімальному розмірі списку."""
fd = nltk.FreqDist(brown.words(categories='science_fiction'))
most_freq_words = fd.keys()[:100]
print most_freq_words

cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='science_fiction'))
likely_tags = dict((word, cfd[word].max()) for word in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags,backoff=nltk.DefaultTagger('NN'))
print baseline_tagger.evaluate(brown_tagged_sents)

baseline_tagger = nltk.UnigramTagger(model=likely_tags)
print baseline_tagger.evaluate(brown_tagged_sents)

def performance(cfd, wordlist):
    lt = dict((word, cfd[word].max()) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='science_fiction'))

def display():
    import pylab
    words_by_freq = list(nltk.FreqDist(brown.words(categories='science_fiction')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='science_fiction'))
    sizes = 2 ** pylab.arange(15)
    perfs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, perfs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()
print display()

"""3.5. Знайдіть розмічені корпуси текстів для інших мов які вивчаєте або володієте (українська, польська, німецька, російська, італійська, японська). Здійсніть тренування та оцініть продуктивність роботи різних аналізаторів та комбінацій різних аналізаторів. Точність роботи аналізаторів порівняйте з точністю роботи аналізаторів для англійських корпусів. Результати поясніть."""
from nltk.corpus import floresta
floresta_tagged_sents = floresta.tagged_sents()
floresta_sents = floresta.sents()

unigram_tagger = nltk.UnigramTagger(floresta_tagged_sents)
print unigram_tagger.tag(floresta_sents[500])
print unigram_tagger.evaluate(floresta_tagged_sents)

bigram_tagger = nltk.BigramTagger(floresta_tagged_sents)
print bigram_tagger.tag(floresta_sents[500])
print bigram_tagger.evaluate(floresta_tagged_sents)

trigram_tagger = nltk.TrigramTagger(floresta_tagged_sents, backoff=bigram_tagger)
print trigram_tagger.tag(floresta_sents[500])
print trigram_tagger.evaluate(floresta_tagged_sents)

"""3.6. Створити аналізатор по замовчуванню та набір юніграм і n-грам аналізаторів. Використовуючи backoff здійсніть тренування аналізаторів на частині корпуса з вправи 3.2. Дослідіть три різні комбінації поєднання цих аналізаторів. Перевірте точність роботи аналізаторів. Визначіть комбінацію аналізаторів з максимальною точністю аналізу. Змініть розмір даних на яких проводилось тренування. Повторіть експерименти для змінених даних для тренування. Результати порівняйти і пояснити."""
text = brown.raw(categories='science_fiction')
tokens = nltk.word_tokenize(text)

default_tagger = nltk.DefaultTagger('NN')
print default_tagger.tag(tokens)[:100]

brown_tagged_sents = brown.tagged_sents(categories='science_fiction')
brown_sents = brown.sents(categories='science_fiction')

unigram_tagger = nltk.UnigramTagger(brown_tagged_sents,backoff=default_tagger)
print '1 kombinacia'
print unigram_tagger.evaluate(brown_tagged_sents)

bigram_tagger1 = nltk.BigramTagger(brown_tagged_sents,backoff=unigram_tagger)
print '2 kombinacia'
print bigram_tagger1.evaluate(brown_tagged_sents)

bigram_tagger2 = nltk.BigramTagger(brown_tagged_sents,backoff=default_tagger)
print '3 kombinacia'
print bigram_tagger2.evaluate(brown_tagged_sents)

trigram_tagger1 = nltk.TrigramTagger(brown_tagged_sents, backoff=bigram_tagger1)
print '4 kombinacia'
print trigram_tagger1.evaluate(brown_tagged_sents)

trigram_tagger2 = nltk.TrigramTagger(brown_tagged_sents, backoff=unigram_tagger)
print '5 kombinacia'
print trigram_tagger2.evaluate(brown_tagged_sents)

trigram_tagger3 = nltk.TrigramTagger(brown_tagged_sents, backoff=default_tagger)
print '6 kombinacia'
print trigram_tagger3.evaluate(brown_tagged_sents)

trigram_tagger4 = nltk.TrigramTagger(brown_tagged_sents, backoff=bigram_tagger2)
print '7 kombinacia'
print trigram_tagger4.evaluate(brown_tagged_sents)

"""3.7. Прочитати стрічку документування функції demo Brill аналізатора. Здійснити експерименти з різними значення параметрів цієї функції. Встановити який взаємозв’язок є між часом тренування (навчання аналізатора) і точністю його роботи."""
from nltk.book import*
help(nltk.tag.brill.demo)
nltk.tag.brill.demo(num_sents=2000, max_rules=200, min_score=3, error_output='errors.out', rule_output='rules.yaml', randomize=False, train=0.8, trace=3)








            






                


