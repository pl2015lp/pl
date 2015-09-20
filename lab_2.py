print '\n >>> Loadaing texts and libraries for task 9-15. Please wait fev sec.<<<'
import nltk
from nltk.book import *
from nltk.probability import *
print '>>> Libraries and texts for task 9-16 had been loaded. <<<'
print '\n'

print '>>> task 1 <<<'

sentence='she sells sea shells by the sea shore'
sentence1=sentence.split()
print "Tongue twister:\n'she sells sea shells by the sea shore' \nhas the words with 'sh'. Thay are:"
for w in sentence1:
	if w.startswith('sh'):
		print w
		
print '\n >>> task 4 <<<'

str1='Khrystyna Vasylivna Stefanko'
print str1
for word in str1:
    str2=str1.replace('y','')
    str2=str2.replace('a','')
    str2=str2.replace('i','')
    str2=str2.replace('e','')
    str2=str2.replace('o','')
while True:
    try:
        a = raw_input ("Lets type 'str2' to see the result without vowels: ")
        if a == 'str2':
            print str2
            break
        else:
            print "Error. Please try again!"
    except Exception:
        print "oops!"
print '\n'

print '\n >>> task 7 <<<'
c=[]
sorted(set([w.lower() for w in text1]))
print "If you use 'sorted(set ...' you will see this: "
c.append(w)
print c
print '\n'
a=[]
sorted([w.lower() for w in set(text1)])
print "And if you want to use 'sorted(... set(...' you will see this: "
a.append(w)
print a

print '\n >>> task 9 <<<'
f = []
for w in text5:
    if len(w) == 4:
        f.append(w)      
fdist = FreqDist(f)

while True:
    try:
        a = raw_input ("Please enter 'fdist' to see outcomes in text5: ")
        if a == 'fdist':
            print fdist
            break
        else:
            print "Error. Please try again!"
    except Exception:
        print "oops!"

voc = fdist.keys()
while True:
    try:
        a = raw_input ("\n Please enter 'voc[:50]' to see first 50 words in text5: ")
        if a == 'voc[:50]':
            print voc[:50]
            break
        else:
            print "Error. Please try again! 50 words will be enough to see keys"
    except Exception:
        print "oops!"

while True:
    try:
        a = raw_input ("\n Oh. 'chat' is the most meaningful word in text5. \nPlease enter fdist['chat'] to see how many word 'chat'")
        if a == "fdist['chat']":
            print (fdist['chat'])
            break
        else:
            print "Something wrong ;(. Please try again!"
    except Exception:
        print "oops!"

while True:
    try:
        a = raw_input ("\n Do you want to see the chart? (Y/N)")
        if a == 'Y':
            print ("Close the window with chart (Figure 1) to continue program.")
            fdist.plot(50, cumulative=True)
            break
        else:
            print "Why not? Maybe Yes?"
    except Exception:
        print "oops!"
        
t = fdist.hapaxes()
while True:
    try:
        a = raw_input ("\n Type 't' to see words which meet only once: ")
        if a == 't':
            print t
            break
        else:
            print "It's not 't'. Try again!"
    except Exception:
        print "oops!"
print '\n'

print '\n >>> task 11 <<<'
s=[]
for w in text6:
    if ((w.endswith('ize')) and ('z' in w) and ('pt' in w) and (w.isupper())):
        s.append(w)
print "\n Finding words with 'z', 'pt', upper letters and endswith 'ize'. Thay are: "
print s
print '\n'
print '\n >>> task 15 <<<'
print '\n >> For text1: '
text1.collocations()
print '\n >> For text4:'
text4.collocations()
print '\n'
a = []
a.append(text1.collocations)
b = []
b.append(text4.collocations)
if (b==a or a==b):
    print 'Collocations are identical'
else:
    print 'Collocations are not identical!'

print 'END'
            
    
