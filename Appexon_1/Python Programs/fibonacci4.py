# def fibonacci(n):
#     if n <=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
#
# n = 9
# for i in range(n):
#     print(fibonacci(i),end=" ")

# def fibonacci(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b,a+b
#     return a
# n = 4
# for i in range(n):
#     print(fibonacci(i),end =" ")

# n = int(input('enter input'))
# a=0
# b =1
# for i in range(n-1):
#     print(a,end = " ")
#     a,b = b,a+b
# print(a)

# n = int(input('enter a number'))
# f= 1
# for i in range(1,n+1):
#     f = f*i
#     print(f'{i}! is {f}')

#fibonacci
n = 5
a=0
b=1
for i in range(n):
    print(a,end = " ")
    a,b=b,a+b
