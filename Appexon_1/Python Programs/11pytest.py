# 5. Write  a Python program to count the number of strings in a list where the string length is 2 or more and the first and last character are the same.


list1 = ['aba', 'abcd','hello','madam','121','bb','2','222']
count = 0
for i in list1:
    if len(i) > 2 and i[0] == i[-1]:
        print(i)
        count = count+1
print(count)
