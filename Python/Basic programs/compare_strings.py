a = 'Apple'
b = 'Guava'

a1 = a.lower()
b1 = b.lower()

a_unique =[]
b_unique=[]

for i in a1:
    if i not in b1:
        a_unique.append(i)
print(a_unique)

for j in b1:
    if j not in a1:
         b_unique.append(j)
print(b_unique)





