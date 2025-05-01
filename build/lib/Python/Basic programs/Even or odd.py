# number = int(input('enter a number '))
#
# if number % 2 == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')


#using a funciton.

def even_or_odd(num):
    if num % 2 == 0:
        return (f'{num} is even')
    else:
        return (f'{num} is odd')

a = even_or_odd(22)
print(a)