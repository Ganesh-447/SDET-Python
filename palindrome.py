p = input('enter a number')

if p[::-1] == p:
    print(f'The number {p} is palindrome')
else:
    print('not a palindrome')