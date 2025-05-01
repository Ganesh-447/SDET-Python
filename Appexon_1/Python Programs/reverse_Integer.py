# n=-1234
#
# result = 0
# negative = False
#
# if n<0:
#     negative = True
#     n=-n
#
# while n!=0:
#     digit = n % 10 #4
#     result = result * 10 + digit
#     n //=10 #removes the last digit.
#
# if negative:
#     result = - result
#
# print(result)




# n= int(input('enter a number')) #-1234
# result = 0
# negative = False
#
# if n<0:
#     negative = True
#     n = -n
#
# while n!=0:
#     digit = n %10 #4
#     result = result * 10 + digit
#     n //= 10
#
# if negative:
#     result = -result
#
# print(result)


n= int(input('enter a number'))
result = 0
negatvie = False


if n<0:
    negatvie = True
    n = -n

while n!=0:
    digit = n %10
    result = result * 10 + digit
    n = n//10

if negatvie:
    result = -result

print(result)




































