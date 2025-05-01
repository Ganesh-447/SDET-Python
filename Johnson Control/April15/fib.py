def fibonacci(n):
    result=[]
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(7))




n=10
a,b=0,1
for _ in range(n):
    print(a,end=' ')
    a,b=b,a+b

a = 25

if a%2==0:
    print('even')
else:
    print('odd')

num =20
if n>1:
    for i in range(2, int(num**0.5)+1):
        if num % i ==0:
            print('not prime')
            break
    else:
        print('is prime')
else:
    print('not prime')

year = 2024
if (year % 4 ==0 and year %100 !=0) or (year % 400==0):
    print('leap year')
else:
    print('not leap year')
