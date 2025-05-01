# a = [1,2,2,3,4,5,5,3]
# b=[]
#
# for i in a:
#     if a.count(i) > 1 and i not in b:
#         b.append(i)
# print(b)
# l1 = [2,4,5,4,6,98,7,6,2]
# l2 =[]
# for i in l1:
#     if l1.count(i)>1 and i not in l2:
#         l2.append(i)
# print(l2)
l1 = [2,3,4,2]
for index,i in enumerate(l1):
    if l1.count(i) > 1:
        print(f'the index is {index} and the values is {i}')
n = 5
k = n-1
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end = " ")
    print()














