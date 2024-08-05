number = int(input('enter a number '))

while number > 10:
    sum =0
    while number >0:
        mod = number % 10    #8     #8                    #6   #1
        sum += mod           #8 + 8 = 16                  #6 + 1 = 7
        number = number // 10  #8 #0  sum = 16.           #1  #0   sum =7
    number = sum #7

print(number)

