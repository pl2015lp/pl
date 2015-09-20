print '>>> task 4 <<<'
print 'Printing joined strings: \n'
msg="Khrystyna Stefanko"
s = "Hello"
b=s + msg
a=s+" "
string=a+msg
print string
print '\n >>> task 8 <<<'
len(b)
print " \n Generate IndexError!!!! "
print string[-25]
print b
print '\n >>> task 9 <<<'
print "\n Make defined step to the string [6:15]"
print string[6:15]
print '>>> task 14 <<<'
print "\n Let me to display the letters of msg string - one per line"
for word in msg:
        print(word)
print '\n >>> task 18 <<<'
ph1=['Khrystyna','Vasylivna','Stefanko']
print "\n Phrase1= "
print ph1
lengths=[]
for word in ph1:
	len(word)
	lengths.append(len(word))
print "\n lengths of phrase1 are: "
print lengths

print '\n >>> task 23 <<<'
silly = 'newly formed bland ideas are inexpressible in an infuriating way'
bland = silly.split()
bland.sort()
print "\n sorted silly"
print bland

print '\n >>> task 24 <<<'
s='inexpressibl'
print "\n Index 'e' in word inexpressibl"
i = s.index('e')
print i
print "\n Index 're' in word inexpressibl"
i=s.index('re')
print i


