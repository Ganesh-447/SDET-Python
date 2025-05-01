# a = [1,2,3,4,5,3]
# b ={}
# for index,i in enumerate(a):
#         if i not in b:
#             b[i]=[]
#             b[i].append(index)
# print(b)
# Given list
arr = [1, 2, 3, 4, 6, 3, 3]
#
# Iterate through the list
for index, element in enumerate(arr):
    # Check if the element appears more than once
    if arr.count(element) > 1:
        # If yes, print the index and value
        print(f"Index: {index}, Value: {element}")

# index
# a = [1,2,3,4,5,3]
# b = []
# for element in a:
#     if a.count(element) > 1 and element not in b:
#         b.append(element)
# print(b)
