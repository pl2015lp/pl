"""16. Напишіть програму для знаходження слів та словосполучень згідно відповідних їм тегів для відповіді на наступне питання: які слова маркуються тегом MD (створити впорядкований за частотою список); """
import nltk
from nltk.probability import FreqDist
from nltk.corpus import state_union
print state_union.fileids()
text = nltk.word_tokenize(state_union.raw('1945-Truman.txt'))
morph_text = nltk.pos_tag(text)

result = [word[0] for word in morph_text if word[1]== 'MD']
print result

print FreqDist(result).keys()

"""3. Опрацювати всі приклади з методичних вказівок по роботі зі словниками. Що станеться, якщо доступитися до неіснуючого запису звичайного словника та словника по замовчуванню?"""
import collections
d = {}
d['house'] = 'big'
d['dog'] = 'Dec'
print d
print d.keys()
print list(d)
print sorted(d)
print 'Mykhailo' in d
for key in d:
    print key

print d.values()
d1 = dict([('Olena',21), ('Oleh','old'), ('Mykhailo', -3)])
print d1
d1.update(d)
print d1
d2 = collections.defaultdict(int)
print d2
print d2['test']
print d2['test1']

"""5. Створити два словники Що станеться зі словниками після виконання команди d1.update(d2)"""
d1 = dict([('I','am'), ('They','are')])
d2 =dict([('you','are'), ('she','is'),])
print d1.update(d2)

"""7. Використовуючи sorted() та set() отримайте відсортований список всіх тегів корпуса Brown без їх дублювання."""
from nltk.corpus import brown
text1 = nltk.word_tokenize(brown.raw())
morph_text1 = nltk.pos_tag(text1)

result1 = sorted(set([word[1] for word in morph_text1]))
print result1[:50]


"""11. Напишіть програму, яка обробить Brown Corpus і допоможе відповісти на наступне запитання: які теги для маркування іменників найчастіше використовуються і що вони означають."""
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news')
print brown_news_tagged[:20]

result3 = [word[1] for word in brown_news_tagged[:20] if word[1].startswith('NN')]
print FreqDist(result3).keys()
print nltk.help.brown_tagset('NN.*')

"""14. Напишіть програму для збору статистичних даних по розмічених корпусах і відповіді на наступне запитання: який відсоток слів корпусу Brown мають неоднозначності."""
brown_news_tagged = brown.tagged_words(categories='news')
morph_dict = {}
homon_count = 0
for word, part in brown_news_tagged[:100]:
    if word in morph_dict.keys():
        morph_dict[word].append(part)
    else:
        morph_dict[word]=[part]

for word in morph_dict.keys():
    if len(set(morph_dict[word])) > 1:
        homon_count += len(morph_dict[word])

print morph_dict
print float(homon_count)/float(len(morph_dict)) * 100

"""18.	Напишіть програми для знаходження слів та словосполучень згідно відповідних їм тегів для відповіді на наступне питання: яке співвідношення між займенниками (чоловічими і жіночими). """
from collections import Counter
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

tagdict = findtags('PP', nltk.corpus.brown.tagged_words(categories='editorial'))
print tagdict

"""21. Написати програму побудови словника, записами якого будуть набори словників. Використовуючи створений словник, збережіть у ньому набори можливих тегів, які зустрічаються після заданого слова з певним тегом, наприклад wordi → tagi → tagi+1."""
#{'word':,{'part1': ['part', 'part'], 'part2': ['part', 'part']}, }
import nltk
from nltk.corpus import brown
position = nltk.defaultdict(dict)
tagging = brown.tagged_words(simplify_tags=True)
for ((word1, tag1), (word2, tag2)) in nltk.bigrams(tagging):
    pos_temp = position[word1].setdefault(tag1, set())
    pos_temp.add(tag2)
    
print position['small'].get('ADJ')
print position['spring'].get('V')
