# number = int(input('enter prime number'))
#
# if number <= 1:
#     print('invalid to process,prime numbers greater than 1')
# elif number == 2:
#         prime = True
# else:
#     prime = True
#     for i in range(2,number):
#         if number % i ==0:
#             prime = False
#
# if prime:
#     print(f'{number} is prime')
# else:
#     print(f'{number} is not prime')

# num = int(input("enter you number"))
#
# if num <= 1:
#     print("not applicable")
# elif num ==2:
#     prime = True
# else:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#
# if prime:
#     print(f'{num} is prime')
# else:
#     print(f'{num} is not prime')



number = int(input('enter a number'))
if number <=1:
    print('not applicable')
elif number ==2:
    prime = True
else:
    prime = True
    for i in range(2,number):
        if number % 2 == 0:
            prime = False
if prime:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')
