strs = ['flower', 'flow', 'flight']
prefix = strs[0]

if not strs:
    print("")

for i in strs[1:]:

    while i[:len(prefix)] != prefix:

        prefix = prefix[:-1]

        if not prefix:
            print("")
print(prefix)







