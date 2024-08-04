number = int(input('enter a number '))
if number > 1:
    for i in range(2,(number//2)+1):
        if (number % i == 0):
            print(f'{number} is not prime number')
            break
    else:
        print(f'{number} is prime')
else:
    print(f'{number} is not prime')
