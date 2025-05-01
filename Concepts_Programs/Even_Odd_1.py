number = int(input('enter a number \n'))

if number % 2 ==0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')



a = lambda x: x ** 2
print(a(9))