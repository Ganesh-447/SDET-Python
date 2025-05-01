# def fact(n):
#     f = 1
#     i = 1
#     while (i<=n):
#         f = f*i
#         i = i +1
#     print(f)
# fact(5)

# def fact(p):
#     if p == 0:
#         return 1
#     return p*fact(p-1)
#
# a= fact(5)
# print(a)

n = int(input('number'))
f = 1
for i in range(1,n+1):
    f = f*i
print(f)