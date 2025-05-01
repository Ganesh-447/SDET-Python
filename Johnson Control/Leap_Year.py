year = int(input("enter the year"))

is_leap_year = False

if (year% 4==0 and year % 100 !=0) or (year % 400 ==0):
    is_leap_year = True

if is_leap_year:
    print(f'{year} is Leap year')
else:
    print(f'{year} is not leap year')