# a =[-2, 1, -3, 4, -1, 2, 1, -5, 4]
# max_sum = float('-inf')
# current_sum = 0
#
# for i in a:
#
#     current_sum += i
#
#     if current_sum > max_sum:
#         max_sum = current_sum
#
#     if current_sum < 0:
#         current_sum = 0
# print(max_sum)
#
# a= [-2,1,-3,4,-1,2,1,-5,4]
# c_sum = 0
# max_sum = float('-inf')
# for i in a:
#     c_sum += i
#     if c_sum > max_sum:
#         max_sum = c_sum
#     if c_sum < 0:
#         c_sum = 0
# print(max_sum)


a= [-2,1,-3,4,-1,2,1,-5,4]
c_sum = 0
max_sum = float('-inf')
for i in a:
    c_sum += i
    if c_sum > max_sum:
        max_sum = c_sum
    if c_sum < 0:
        c_sum = 0
print(max_sum)




