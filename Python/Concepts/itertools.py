from itertools import *
list1 =[1,2,3,'abc','ab']
list2=[89,32,23,'test','oman']

for i in (list1,list2):
    print(i)

for i in chain(list1,list2):
    print(i)
print(list(chain(list1,list2)))

#count

for i in count(10,2.5):
    if i <= 50:
        print(i)
    else:
        break

b = range(10,13)
for i in cycle(b):
    print(i)