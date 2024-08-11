# string_1 = 'Tooth Paste'
# n = len(string_1)
# list1=[]
# for i in range(n):
#     for j in range(i+1,n):
#         if string_1[i] == string_1[j] and string_1[i] not in list1:
#             if string_1[i] == ' ':
#                 pass
#             else:
#                 list1.append(string_1[i])
# print(list1)


a = 'ganesh ankarao grandhi'
b=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]== a[j] and a[i] not in b:
            b.append(a[i])
print(b)