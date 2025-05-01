numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(num):
    return  num %2 ==0


even_num= filter(is_even,numbers)
a=list(even_num)
print(a)


#program-2

a=['apple','goat','gangtok','nagaland','kohima']
min_len=6

def check_len(word):
    return len(word)>min_len

print(list(filter(check_len,a)))

d=list(filter(lambda var: len(var)>min_len, a))
print(d)


#Using Lambda.

numList=[1,-20,90,-99,100,40]

num_greater_than_10 = list(filter(lambda num:num >10 , numList))
print(num_greater_than_10)