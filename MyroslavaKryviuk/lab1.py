str = 'My name is Myroslava'
sent = str.split()
my_list = list()

for i in reversed(sorted(sent, key=len)):
   my_list.append(i)

print(my_list)

