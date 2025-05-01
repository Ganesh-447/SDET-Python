#reverse a string
# name= input('enter a string')
# n = len(name)
# test =''
#
# for i in range(n-1,-1,-1):
#     test += name[i]
#
# print(test)

#print(name[::-1]) -
# Reverse

r_name ="Good Morning"
test1= r_name.split()
print(test1)
test2=[i[::-1] for i in test1]
a=' '.join(test2)
print(a)