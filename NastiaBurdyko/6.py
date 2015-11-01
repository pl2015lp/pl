Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
#1,2,3,4,5,6 Описати, які класи стрічок відповідають наступним регулярним виразам
>>> from __future__ import division
>>> import nltk, re, pprint
>>> word= 'Look at this function'
>>> nltk.re_show (r'[a-zA-Z]+', word)
{Look} {at} {this} {function}
#Виділяє всі слова, які складаються з літер, але не виділяє цифри і розділові знаки.
>>> word = 'hey, look at this Function'
>>> nltk.re_show(r'[A-Z][a-z]*', word)
hey, look at this {Function}
#Виділяє лише слова, які починаються з великої літери.
>>> numbers= '12, 13.000,  14.01, 1500, 4/3'
>>> nltk.re_show(r'\d+(\.\d+)?', numbers)
{12}, {13.000},  {14.01}, {1500}, {4}/{3}
#Виділяє послідовність цифр.
>>> word = 'appearance, accessorize, jewellery'
>>> nltk.re_show(r'([^aeiou][aeiou][^aeiou])*', word)
{}a{}p{}p{}e{}a{rance, accessor}i{ze,} {jew}e{}l{ler}y{}
#Виділяється послідовності символів, що складаються з трьох символів, перший і третій з яких не є голосною, а другий – будь-яка голосна з [aeiou] і зустрічаються 0 і більше разів.
>>> word = 'walkie-talkie, boogie-moogie, funny'
>>> nltk.re_show(r'\w+|[^\w\s]+', word)
{walkie}{-}{talkie}{,} {boogie}{-}{moogie}{,} {funny}
#Виділяє всі слова, цифри та символи.
>>> word= 'pit, pot, pot, pint, put'
>>> nltk.re_show(r'p[aeiou]{,2}t', word)
{pit}, {pot}, {pot}, pint, {put}
#Bиділяє стрічку, які складаються з літери “p”, від 0 до 2 голосних і літери 

#8.Написати регулярний вираз, який встановлює відповідність наступному класу стрічок:арифметичний вираз з цілими значеннями і, який містить операції множення та додавання (2*3+8).

>>> l='2*3+8'
>>> nltk.re_show (r"\d+[+|*]\d+[+|*]\d+", l)
{2*3+8}

#9.Зберегти довільний текст у файлі corpus.txt. Визначити функцію  для читання з цього файлу (назва файлу аргумент функції) і повертає стрічку, яка містить текст з файлу. Використовуючи nltk.regexp_tokenize() розробити токенізатор для токенізації різних типів пунктуації в цьому тексті. Використовувати багаторядковий запис регулярного виразу з коментарями та «verbose flag» 
import nltk, re, pprint
def MyLoad(fl,text):
        for line in f:
           print line.strip()
        f = open('I:\Corpus.txt')
f = open('I:\Corpus.txt')
raw = f.read()
print 'TEXT:'
print raw
print 'TOKENIZED TEXT'
pattern = r'''(?x)    # set flag to allow verbose regexps
     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
   | \w+(-\w+)*        # words with optional internal hyphens
   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
   | \.\.\.            # ellipsis
   | [][.,;"'?():-_`]  # these are separate tokens
 '''
print nltk.regexp_tokenize(raw, pattern)
TEXT:
Amazon is taking legal action against more than 1,000 people it says have posted fake reviews on its website.

The US online retail giant has filed a lawsuit in Seattle, Washington.

It says its brand reputation is being damaged by "false, misleading and inauthentic" reviews paid for by sellers seeking to improve the appeal of their products.

It comes after Amazon sued a number of websites in April for selling fake reviews.

Amazon says the 1,114 defendants, termed "John Does" as the company does not yet know their real names, offer a false review service for as little as $5 (?3.24) on the website Fiverr.com, with most promising five-star reviews for a seller's products.

"While small in number, these reviews can significantly undermine the trust that consumers and the vast majority of sellers and manufacturers place in Amazon, which in turn tarnishes Amazon's brand," the technology giant said in its complaint, which was filed on Friday.

Amazon said it had conducted an investigation, which included purchasing fake customer reviews on Fiverr from people who promised five-star ratings and offered to allow purchasers to write reviews. 
TOKENIZED TEXT
['Amazon', 'is', 'taking', 'legal', 'action', 'against', 'more', 'than', '1', ',', '000', 'people', 'it', 'says', 'have', 'posted', 'fake', 'reviews', 'on', 'its', 'website', '.', 'The', 'US', 'online', 'retail', 'giant', 'has', 'filed', 'a', 'lawsuit', 'in', 'Seattle', ',', 'Washington', '.', 'It', 'says', 'its', 'brand', 'reputation', 'is', 'being', 'damaged', 'by', '"', 'false', ',', 'misleading', 'and', 'inauthentic', '"', 'reviews', 'paid', 'for', 'by', 'sellers', 'seeking', 'to', 'improve', 'the', 'appeal', 'of', 'their', 'products', '.', 'It', 'comes', 'after', 'Amazon', 'sued', 'a', 'number', 'of', 'websites', 'in', 'April', 'for', 'selling', 'fake', 'reviews', '.', 'Amazon', 'says', 'the', '1', ',', '114', 'defendants', ',', 'termed', '"', 'John', 'Does', '"', 'as', 'the', 'company', 'does', 'not', 'yet', 'know', 'their', 'real', 'names', ',', 'offer', 'a', 'false', 'review', 'service', 'for', 'as', 'little', 'as', '$5', '(', '?', '3', '.', '24', ')', 'on', 'the', 'website', 'Fiverr', '.', 'com', ',', 'with', 'most', 'promising', 'five-star', 'reviews', 'for', 'a', 'seller', "'", 's', 'products', '.', '"', 'While', 'small', 'in', 'number', ',', 'these', 'reviews', 'can', 'significantly', 'undermine', 'the', 'trust', 'that', 'consumers', 'and', 'the', 'vast', 'majority', 'of', 'sellers', 'and', 'manufacturers', 'place', 'in', 'Amazon', ',', 'which', 'in', 'turn', 'tarnishes', 'Amazon', "'", 's', 'brand', ',', '"', 'the', 'technology', 'giant', 'said', 'in', 'its', 'complaint', ',', 'which', 'was', 'filed', 'on', 'Friday', '.', 'Amazon', 'said', 'it', 'had', 'conducted', 'an', 'investigation', ',', 'which', 'included', 'purchasing', 'fake', 'customer', 'reviews', 'on', 'Fiverr', 'from', 'people', 'who', 'promised', 'five-star', 'ratings', 'and', 'offered', 'to', 'allow', 'purchasers', 'to', 'write', 'reviews', '.']
>>> 

#11.Написати функцію unknown(), яка приймає інтернет адресу як аргумент і повертає невідомі слова, які зустрічаються в тексті. При розробці функції використовувати re.findall() для виявлення всіх підстрічок та корпус Words Corpus (nltk.corpus.words) для виявлення не відомих слів.
from __future__ import division
import urllib, nltk
from urllib import urlopen
url="http://www.bbc.com/news/science-environment-34540414"
raw_contents=urllib.urlopen(url).read()
raw=nltk.clean_html(raw_contents)
tokens=nltk.word_tokenize(raw)
print tokens
import nltk, re
def unknown(text):
    wordlist = [w for w in nltk.corpus.words.words('en')]
    new_text = re.findall(r"[A-Za-z]+", raw)
    print new_text
    print
    print 'UNKNOWN WORDS:'
    for w in new_text:
        if w not in wordlist:
            print w
text='Corpus.txt'
unknown(text)
 ================================
>>> 
['Permafrost', 'warming', 'in', 'parts', 'of', 'Alaska', "'is", 'accelerating', "'", '-', 'BBC', 'News', 'Accessibility', 'links', 'Skip', 'to', 'content', 'Accessibility', 'Help', 'BBC', 'iD', 'BBC', 'navigation', 'News', 'News', 'Sport', 'Weather', 'Shop', 'Earth', 'Travel', 'Capital', 'iPlayer', 'Culture', 'Autos', 'Future', 'TV', 'Radio', 'CBBC', 'CBeebies', 'Food', 'Arts', 'Make', 'It', 'Digital', 'iWonder', 'Bitesize', 'Music', 'Nature', 'Earth', 'Local', 'Travel', 'Menu', 'Search', 'the', 'BBC', 'BBC', 'News', 'News', 'navigation', 'Sections', 'Home', 'Video', 'World', 'UK', 'Business', 'Tech', 'Science', 'selected', 'Magazine', 'Entertainment', '&', 'amp', ';', 'Arts', 'Health', 'In', 'Pictures', 'Also', 'in', 'the', 'News', 'Special', 'Reports', 'Explainers', 'The', 'Reporters', 'Have', 'Your', 'Say', 'Science', '&', 'Environment', 'Science', '&', 'Environment', 'Permafrost', 'warming', 'in', 'parts', 'of', 'Alaska', "'is", 'accelerating', "'", 'By', 'Matt', 'McGrath', 'Environment', 'correspondent', ',', 'BBC', 'News', '22', 'October', '2015', 'From', 'the', 'section', 'Science', '&', 'amp', ';', 'Environment', 'Image', 'copyright', 'Science', 'Photo', 'Library', 'Image', 'caption', 'Houses', 'like', 'this', 'one', 'near', 'Fairbanks', 'have', 'collapsed', 'because', 'of', 'permafrost', 'melt', 'One', 'of', 'the', 'world', "'s", 'leading', 'experts', 'on', 'permafrost', 'has', 'told', 'BBC', 'News', 'that', 'the', 'recent', 'rate', 'of', 'warming', 'of', 'this', 'frozen', 'layer', 'of', 'earth', 'is', '``', 'unbelievable', "''", '.', 'Prof', 'Vladimir', 'Romanovsky', 'said', 'that', 'he', 'expected', 'permafrost', 'in', 'parts', 'of', 'Alaska', 'would', 'start', 'to', 'thaw', 'by', '2070.', 'Researchers', 'worry', 'that', 'methane', 'frozen', 'within', 'the', 'permafrost', 'will', 'be', 'released', ',', 'exacerbating', 'climate', 'change', 'The', 'professor', 'said', 'a', 'rise', 'in', 'permafrost', 'temperatures', 'in', 'the', 'past', 'four', 'years', 'convinced', 'him', 'warming', 'was', 'real.', 'Permafrost', 'is', 'perennially', 'frozen', 'soil', 'that', 'has', 'been', 'below', 'zero', 'degrees', 'C', 'for', 'at', 'least', 'two', 'years.', 'It', 'was', 'assumed', 'it', 'would', 'be', 'stable', 'for', 'this', 'century', 'but', 'it', 'seems', 'that', "'s", 'not', 'true', 'any', 'more', 'Prof', 'Vladimir', 'Romanovski', ',', 'University', 'of', 'Alaska', 'It', "'s", 'found', 'underneath', 'about', '25', '%', 'of', 'the', 'northern', 'hemisphere', ',', 'mainly', 'around', 'the', 'Arctic', '-', 'but', 'also', 'in', 'the', 'Antarctic', 'and', 'Alpine', 'regions.', 'It', 'can', 'range', 'in', 'depth', 'from', 'one', 'metre', 'under', 'the', 'ground', 'all', 'the', 'way', 'down', 'to', '1,500m.', 'Media', 'caption', 'The', 'BBC', "'s", 'Matt', 'McGrath', 'explores', 'the', 'permafrost', '``', 'time', 'tunnel', "''", 'Scientists', 'are', 'concerned', 'that', 'in', 'a', 'warming', 'world', ',', 'some', 'of', 'this', 'permanently', 'frozen', 'layer', 'will', 'thaw', 'out', 'and', 'release', 'methane', 'gas', 'contained', 'in', 'the', 'icy', ',', 'organic', ....]
UNKNOWN WORDS:
Permafrost
parts
accelerating
BBC
News
Accessibility
Skip
Accessibility...
            
15. Прочитати Додаток А. Дослідити явища описані у Додатку А використовуючи корпуси текстів та метод findall()для пошуку в токенізованому тексті. 

import nltk
from nltk.corpus import gutenberg, nps_chat, brown
blake=nltk.Text(gutenberg.words('blake-poems.txt'))
print blake.findall(r'<the> <best> (<.*>) <can>')
chat = nltk.Text(nps_chat.words())
print chat.findall(r'<the> <best> (<.*>) <can>')
brown1=nltk.corpus.brown(categories='news')
print brown1.findall(r'<the> <best> (<.*>) <can>')

