#Case -1: Print string in reverse without loops
# a = 'good morning'
# n = len(a)
# b = ''
# for i in range(n-1,-1,-1):
#     b += a[i]
# print(b)  #gninrom doog

#same with concept of slicing.
# a ='good morning'
# print(a[::-1])

# good morning to morning good. without using any functions.

# name ='good morning'
# l = len(name)
# list1 = []
# string1=''
# for i in range(l):
#     if name[i] != ' ':
#         string1 += name[i]
#     else:
#         list1.append(string1)
#         string1 =''
# list1.append(string1)
# print(list1)
# reversed_string = ''
# length = len(list1)
# for i in range(length-1,-1,-1):
#     print(list1[i])
#     reversed_string += list1[i]
#     if i!=0:
#         reversed_string += ' '
# print(reversed_string) #morning good

#good morning to morning good. using list.

# variable = 'good morning'
# list1 = variable.split()
# length = len(list1)
# test = ''
# for i in range(length-1,-1,-1):
#     test += list1[i]
#     if i!=0:
#         test += ' '
# print(test) #morning good.

#good morning to doog gninrom without functions.

# a = 'good morning'
# list1 = []
# word=''
# n=len(a)
# for i in range(n):
#     if a[i]!= ' ':
#         word += a[i]
#     else:
#         reversed_word =''
#         for j in range(len(word)-1,-1,-1):
#             reversed_word += word[j]
#         list1.append(reversed_word)
#         word=''
# reversed_word = ''
# for j in range(len(word)-1,-1,-1):
#     reversed_word += word[j]
# list1.append(reversed_word)
# print(list1)
# string2 = ' '.join(list1)
# print(string2) #doog gninrom

#same with function.

# a ='good morning'
# list1=a.split()
# b = [i[::-1]for i in list1]
# print(' '.join(b)) #doog gninrom



# a = 'good morning'
# #print(a[::-1])
#
# b = a.split()
# c =[i[::-1] for i in b]
# print(' '.join(c))

a='good morning'
b=''
c=[]
for i in range(len(a)):
    if a[i] != ' ':
        b += a[i]
    else:
        d=''
        for i in range(len(b)-1,-1,-1):
            d += b[i]
        c.append(d)
        b=''
d=''
for i in range(len(b)-1,-1,-1):
    d += b[i]
c.append(d)
print(' '.join(c))













