# 1. Write a Python program to find the largest number in a list.
# 2. Write a Python program to find the smallest number in a list.
# 3. Write a Python program to sum all numbers in a list.
# 4. Write a Python program to multiply all numbers in a list.

a = [2,3,43,3,1]
# print(min(a))
# print(max(a))

small = a[0]
for i in a[1:]:
    if i < small:
        small = i
print(small)