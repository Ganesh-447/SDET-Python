# x = "hello python"
# print(x.split('o'))
# print(len(x.split('o')))
x = "Hello Python"

if x.startswith("H") and len(x) > 12:

	print("'/'.join(x[:7])")

elif x[-1] == "n" and len(x.split('o')) >= 3:

    print(x.lower()[4:])

else:
   print((x + ' ') * 3 + "!")