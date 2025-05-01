# def add(l):
#     sum = 0
#     for i in l:
#         sum += i
#     return sum
# def avg(add,n):
#     res = add/n
#     print(res)
# l =[1,2,3]
# n =2
# avg(add(l),2)
# l =[]
# while True:
#     x = int(input('enter a number'))
#     l.append(x)
#     print("1 to continue,2 to stop")
#     ch = int(input('enter you option'))
#     if ch == 1:
#         continue
#     elif ch ==2:
#         break
#     print("invalid value entered")
#     break
# ans = add(l)
# print(ans)
# n = len(l)
# b = avg (ans,n)
# print(b)

#without function
a = input('enter numbers with spaces')
l = [int(i) for i in a.split()]
#n = len(l)
#a = [1,2,3,4,5]
sum = 0
for i in l:
    sum = sum + i

print(sum)

# a = input('enter ')
#
# l = [int(i) for i in a.split(' ')]
# print(l)
# print(type(a))
# print(type(l))




















