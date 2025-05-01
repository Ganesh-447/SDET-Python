


# def two_string_comparison(a, b):
#     c = a.lower()
#     d = b.lower()
#     r1 = []
#     r2 = []
#     for i in c:
#         if i not in d:
#             r1.append(i)
#     for j in d:
#         if j not in c:
#             r2.append(j)
#
#     print(r1, r2)
#     return r1, r2


# a = input('enter a string')
# b = input('enter a string')
# two_string_comparison(a, b)

# a1 = 'apple'
# b1 = 'strip'
# r1 =[]
# r2 = []
#
# for i in a1:
#     if i not in b1:
#         r1.append(i)
# print(r1)
# for j in b1:
#     if j not in a1:
#         r2.append(j)
# print(r2)


a = 'Apple'
b = 'Strip'
a1 = a.lower()#apple
b1 = b.lower()#strip
r1 = []
r2 = []
for i in a1:
    if i not in b1:
        r1.append(i)

for j in b1:
    if j not in a1:
        r2.append(j)

print(r1)
print(r2)











