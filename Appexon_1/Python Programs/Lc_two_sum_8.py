# num = input('enter a list with spaces')
# nums = list(map(int,num.split()))
# target = int(input('enter a number'))
# n = len(nums)
#
# for i in range(n-1):
#     for j in range(i+1,n):
#         if nums[i] + nums [j] == target:
#             print(f'the numbers which added produces target is {nums[i],nums[j]}and there respective indices are {i,j}')


a = input('enter number with spaces')
nums =[int(i) for i in a.split()]
#print(nums)
target = int(input('enter the target'))
n = len(nums)
for i in range(n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            print(i,j)
