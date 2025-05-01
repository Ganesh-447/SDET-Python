# num = int(input('enter the number'))
#
# while num>=10:
#     sum = 0
#     while num > 0:
#         mod = num % 10
#         sum = sum + mod
#         num= num//10
#     num = sum
# print(sum)

# num = int(input('enter your number'))
#
# while num >10:
#     sum = 0
#     while num > 0:
#         mod = num % 10
#         sum += mod
#         num = num//10
#     num = sum
# print(sum)

#factorial
# num = 5
# f = 1
# for i in range(1,num+1):
#     f = f * i
#     print(f'{i}! is {f}')

# n = 88
#
# while n >10:
#     sum = 0
#     while n > 0:
#         mod = n%10
#         sum = sum + mod
#         n = n//10
#     n = sum
# print(sum)


number = 88
while number > 10:
    sum = 0
    while number > 0:
        mod = number % 10 #gives remainder 8
        sum = sum + mod # 0 + 8 = 8,
        number = number // 10 #removes the last number, so 8
    number = sum
print(sum)

















