nums_input = input('enter numbers with commas')

nums = [int(num) for num in nums_input.split(',')]

target = int(input('enter the target'))

print(f'the list is {nums} and target is {target}')

n = len(nums)

for i in range(n-1):       # a = [2,7,11,15] , target = 9
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            print(f'the indices are {[i,j]} and the values are {[nums[i],nums[j]]}')





#a = [4,5,6,4,8]


