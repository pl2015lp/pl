#2 ???????? ?????? sentence ? ????????? ?? ???????? �she sells sea shells by the sea shore�
?? ???????? ???????? ???????? ??? ????????? ?? ????? ???? ?????, ??????? ????
?????? ??? 4 ???????.

sentence= 'she sells sea shells by the sea shore'
sentence=sentence.split (" ")
sentence.sort ()
print (sentence)
length=[]
for word in sentence:
    print len(word),word

for word in sentence:
    if len (word)>4:
        print (word)
#4 ???????? ????????, ??? ??????? ??? ??????? ?? ???????, ??? ??????????
?????, ?? ???????? ?? ???????? ????????. ???????? ??????? ??????????? ????????
????????????? ???: ????????? ?????????? ???????; ????????? ???????, ? ???? ????
??????????? ?????????; for ???? ??? ??????? ??????? ?????? ?? ???????? ? ??????
?????????? ???????? ? ??????????? ???????.

s = "Kryyyyyyviuk Myroslava Petrivna";
l = list(s);
result=[]
holosni=['a', 'o', 'u', 'y', 'i', 'e']
for index, word in enumerate(l):
    flag = 0
    for letter in holosni:
        if word == letter:
            flag = 1
    if flag == 1:
        del l[index]

print(result)
print(l)

#7 ???????? ???????? ???????? ? ???????? ???? ???????? ????? ?????????? (????? ?
??????? ???????)
	sorted(set([w.lower() for w in text1]))
	sorted([w.lower() for w in set(text1)])

#sorted(set([w.lower() for w in text1]))-??????? ????? ? ?????? ???? ???????? ? ????? ??????, ?????? ?? ???????? ????? ?? ????????????
#sorted([w.lower() for w in set(text1)])- ??????? ????? ? ?????? ???? ???????? ? ????? ??????, ?????? ?? ???????? ????? ????????????

#9 3.9.	???????? ? ?????? ? 5 ??? ????? ??????? ???? ???????? 4 ? ????????? ??? ??? ????????? ????????.

import nltk
from nltk.book import*
fdist=FreqDist(text5)
sorted([w for w in set(text5)
	if len(w)==4])
V = set(text5)
words=[w for w in V if len(w)==4]
sorted(words)
fdist=FreqDist(text5)
print fdist


#11 ???????? ????? ??? ??????????? ? ?????? ?6 ???? ???? ??? ????????????
????????? ???????: ???????????? ?? ize; ??????? ?????? z; ??????? ?????????????
????? pt; ???????? ? ??????? ?????? .
????????? ???????????, ?? ?????? ????.

fdist6=FreqDist(text6)
spysok=['']
spysok = sorted ([w for w in set(text6) if 'z' in w or 'pt' in w or w.endswith('ow')or w.istitle()])
for word in spysok:
    print word

#18 ????????? ????????? ??? ??????? ?1 ?? ?7. ?????????? ??????????.
import nltk
from nltk.book import*
text1.collocations()
print '\n >> For text1:'
text7.collocations()
print '\n >> For text7:'
a = []
a.append(text1.collocations)
b = []
b.append(text7.collocations)
if (b==a or a==b):
    print 'Collocations are identical'
else:
    print 'Collocations are not identical!'
