# number = int(input('enter a number '))
# if number > 1:
#     for i in range(2,(number//2)+1):
#         if (number % i == 0):
#             print(f'{number} is not prime number')
#             break
#     else:
#         print(f'{number} is prime')
# else:
#     print(f'{number} is not prime')
# a = int(input('enter your number'))
#
# if a >2:
#     for i in range(2, a//2+1):
#         if i % a == 0:
#             print('number is not prime')
#         else:
#             print('number is prime')
# else:
#     print('number is not prime')



# number = int(input('enter a number'))
# if number > 1:
#     for i in range(2,(number//2)+1):
#
#         if (number % i == 0):
#             print('its not a prime number')
#             break
#     else:
#          print('its a prime')
# else:
#     print('number is not prime')




number = int(input('enter the number'))

if number >1:
    for i in range(2,(number//2)+1):
        if number % i == 0:
            print('not prime')
            break
    else:
        print('its prime')
else:
    print('enter more than 1')