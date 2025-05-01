nums_input = input('enter list of inputs separated with space')
nums = [int(i) for i in nums_input.split()]
print(nums)
target = int(input('enter the target number'))
n = len(nums)

for i in range(n-1):         #nums = [2,7,9,11] target = 16
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print(f' the indices are {[i,j]} and the values {[nums[i],nums[j]]}')


