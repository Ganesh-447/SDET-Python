a ='ganesh ankarao'
length = len(a)
count = []
for i in range(length):
    for j in range(i+1,length):
        if a[i] == a[j] and a[i] not in count:
            count.append(a[i])
print(count)
