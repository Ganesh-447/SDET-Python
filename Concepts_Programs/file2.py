

try:
    file_1=open('ganeshgrandhi.txt','r')
    print(file_1.read())

except Exception as E:
    print(f'Please try again by correcting the error {E}')
finally:
    try:
        file_1.close()
    except Exception as Error:
        print(f'{Error}')