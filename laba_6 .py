from __future__ import division
import nltk, re, pprint

print "\n<<<task 1>>>"
a=nltk.re_show('[a-zA-Z]+','That famous Monty Python Company, costed $1123.13 in 12.04.1968.')
print a
#{That} {famous} {Monty} {Python} {Company}, {costed} $1123.13 {in} 12.04.1968.
##########################################################################

print "\n<<<task 2>>>"
b=nltk.re_show('[A-Z][a-z]*','That famous Monty Python Company, costed $1123.13 in 12.04.1968.')
print b
# {That} famous {Monty} {Python} {Company}, costed $1123.13 in 12.04.1968.

##############################################################################

print "\n<<<task 3>>>"
c=nltk.re_show('\d+(\.\d+)?','That famous Monty Python Company, costed $1123.13 in 12.04.1968.')
print c
#That famous Monty Python Company, costed ${1123.13} in {12.04}.{1968}.

########################################################################################
print "\n<<<task 4>>>"
d=nltk.re_show('([^aeiou][aeiou][^aeiou])*','Does your boss seem to favor your administrative professional coworker and think the sun rises and sets with her (or him)?')
print d
# {}D{}o{}e{}s{} {}y{}o{}u{}r{} {bos}s{} {}s{}e{}e{}m{} {to fav}o{}r{} {}y{}o{}u{}r{ admin}i{}s{}t{rat}i{ve }p{rof}e{}s{}s{}i{}o{nal} {cow}o{}r{ker an}d{} {}t{hin}k{} {}t{he sun}
#{ris}e{}s{ an}d{} {set}s{} {wit}h{} {her} {(or} {him}){}?{}

######################################################################################

print "\n<<<task 5>>>"
e=nltk.re_show('\w+|[^\w\s]+.','In astronomy and cosmology, dark matter is a type of matter hypothesized to account for a large part of the total mass in the universe.')
print e 
#{In} {astronomy} {and} {cosmology}{, }{dark} {matter} {is} {a} {type} {of} {matter} {hypothesized} {to}
#{account} {for} {a} {large} {part} {of} {the} {total} {mass} {in} {the} {universe}.

##############################################################################################################

print "\n<<<task 6>>>"
f=nltk.re_show('p[aeiou]{,2}t','In astronomy and cosmology, dark matter is a type of matter hypothesized to account for a large part of the total mass in the universe.')
print f
#In astronomy and cosmology, dark matter is a type of matter hy{pot}hesized to account for a large part of the total mass in the universe.

#################################################################################################################

print "\n<<<task 7>>>"
chat_words=sorted(set(w for w in nltk.corpus.nps_chat.words()))
articles=[w for w in chat_words if re.search('^(an?|the)$',w)]# '?' вказує на опціональність, тобто а і an
print articles
#['a', 'an', 'the']

##########################################################################

print "\n<<<task 9>>>"
def Mytext (t):
    w=''
    for line in t:
        a=line.strip()
        str=a
    return str
f= open ('E:\Text\corpus.txt')
#>>> Mytext(f)
#Communication is simply the act of transferring information from one place to another, whether this be vocally (using voice),
#written (using printed or digital media such as books, magazines, websites or emails),
#visually (using logos, maps, charts or graphs) or non-verbally (using body language, gestures and the tone and pitch of voice).
text=f.read()
print text

pattern=r'''(?x)    # set flag to allow verbose regexps
...     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
...   | \w+(-\w+)*        # words with optional internal hyphens
...   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
...   | \.\.\.            # ellipsis
...   | [][.,;"'?():-_`]  # these are separate tokens
[][.,;"'?():-_`]  # these are separate tokens
...'''
print nltk.regexp_tokenize(text,pattern)
#['Communication is', 'simply th', 'e ac', 't of', 'transferring in', 'formation fr', 'om on', 'e pl', 'ace to', 'another, w',
# 'hether th', 'is be', 'vocally (u', 'sing vo', 'ice), ', 'written (u', 'sing pr', 'inted or', 'digital me', 'dia su', 'ch as',
# 'books, m', 'agazines, w', 'ebsites or', 'emails), ', 'visually (u', 'sing lo', 'gos, m', 'aps, c', 'harts or', 'graphs) o',
# 'r no', 'n-verbally (u', 'sing bo', 'dy la', 'nguage, g', 'estures an', 'd th', 'e to', 'ne an', 'd pi', 'tch of', 'voice).']

######################################################################################################################################

print "\n<<<task 11 >>>"
import urllib, nltk
from urllib import urlopen
def Unknown (url):
           html=urlopen(url).read()
           raw=nltk.clean_html(html)
           un_words=nltk.corpus.words.words()
           if re.findall(r'[A-Za-z]*',raw) not in un_words:
               return re.findall(r'[A-Za-z]*',raw)
print Unknown ("http://news.bbc.co.uk/2/hi/health/2284783.stm")

######################################################################################################################################

print "\n<<<task 15 >>>"
from nltk.corpus import gutenberg, nps_chat
text=nltk.Text(gutenberg.words('milton-paradise.txt'))
print text.findall(r'<as> <best> <\w*> <can>')
print text.findall(r'<as> <best> <as> <\w*> <can>')
chat_w = nltk.Text(nps_chat.words())
print chat_w.findall(r'<as> <best> <\w*> <can>')
print chat_w.findall(r'<as> <best> <as> <\w*> <can>')

#None

#None

