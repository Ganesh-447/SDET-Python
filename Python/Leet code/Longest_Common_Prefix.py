str_1 =["flower", "flow", "flight"]

if not str_1:
    print('')
prefix = str_1[0]
#print (prefix)
for string in str_1[1: ]:
    while string[:len(prefix)] != prefix:

        prefix = prefix[:-1]
        if not prefix:
            print('')
print(prefix)





