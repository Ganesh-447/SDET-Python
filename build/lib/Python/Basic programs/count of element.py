# a ='apple'
# repeated_words ={}
#
# for char in a:
#     if char in repeated_words:
#         repeated_words [char] += 1
#     else:
#         repeated_words [char] =1
# #print(repeated_words)
# dic_1 ={char:count for char,count in repeated_words.items() if count>1 }
# print(dic_1)

# a= 'ganesh grandhi'
# key_value ={}
# for char in a:
#     if char in key_value:
#         key_value[char] += 1
#     else:
#         key_value[char] =1
# r ={char:count for char,count in key_value.items() if count >1 }
# print(r)

# a='ganesh ankarao'
# d ={}
# for i in a:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] =1
# dic = {i:count for i,count in d.items() if count >1}
# print(dic)



a = 'apple'
d ={}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
c = {i:count for i,count in d.items() if count >1}
print(c)












