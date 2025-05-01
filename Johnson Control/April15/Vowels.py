abc=input('enter a string')
count=0
new=""
vowel="aeiouAEIOU"
for i in abc:
    if i in vowel:
        count += 1
        if i not in new:
            new += i
print(f'it has {count} count and unique letters are {new}')



