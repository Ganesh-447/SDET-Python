pal=input('enter a input')
n= len(pal)
p=""
for i in range(n-1,-1,-1):
    p += pal[i]
print(p)

if pal == p:
    print(f'{pal} is palindrome')
else:
    print(f'{pal} is not a palindrome')

#using function.

def palindrom(user_input):
    new_input=""
    for ch in user_input:
        new_input = ch + new_input
    return new_input

