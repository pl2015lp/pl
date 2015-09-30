import urllib, nltk
from urllib import urlopen

print '========= Task 1 ========='
link = "http://www.nltk.org/"
data = urlopen(link).read()
raw = nltk.clean_html(data)
t = nltk.word_tokenize(raw)
print 'Text of loaded and parssed url: \n', t[:30]

print '\n ========= Task 2 ========='
path  = 'C:\py'
f = open(path+'\corpus.txt','w')
for w in t:
    f.write(w+' ')
f.close()
newf = open(path+'\corpus.txt', 'r')
data = newf.read()
print 'String from file corpus.txt: \n', data[:187], '...'



print '\n ========= Task 4 ========='

a="3"
print 'The first case: "3" * 7 =', a*7
print 'The second case: 3 * 7 =', 3*7
print 'Conversation int("3") =', int("3")
print 'Conversation str(3) =' , str(3)

print '\n ========= Task 5 ========='
print '6 spaces before:','%6s' % 'str'
print '6 spaces after:','%-6s' % 'str'
