msg='Myroslava Kryviuk'
print (msg)

a = msg [1::2]
print (a)

s='colorless'
print (s)
b=s[0:4]+'u'+s[4:]
print (b)

phrase1=['Myroslava', 'Petrivna', 'Kryviuk']
print (phrase1)
print (phrase1[2][2])

lengths=[]
for word in phrase1:
    print len(word),word

for word in phrase1:
    lengths.append(len(word))

print(lengths)

silly='newly formed bland ideas are inexpressible in an infuriating way'
silly = silly.split (" ")
silly.sort()
print (silly)
filtered = []
for word in silly:
    if word !="in":
        filtered.append(word)
print(filtered)