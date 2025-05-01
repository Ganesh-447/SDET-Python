n=int(input('enter the number\n'))
result = 0
negative = False

if n <0:
    negative = True
    n = -n

while n!= 0:
    digit = n %10
    result = result * 10 + digit
    n = n//10

if negative:
    result = -result

print(result)
