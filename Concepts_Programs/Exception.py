a=10

try:
    b = int(input('enter a number'))
    c=a/b
    print(f'result{c}')
except Exception as E:
    print(f'Error is {E}')
else:
    print(f'you are successfull')
finally:
    print(f'the end')

# except ZeroDivisionError:
#     print('Error: Division by zero is not allowed')
# except ValueError:
#     print('Error: Invalid input,please enter valid interger')
# except Exception as E:
#     print('Error')