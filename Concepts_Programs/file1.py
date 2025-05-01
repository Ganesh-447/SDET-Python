

file1 = open('ganesh.txt','r')
print(file1.read())
file1.close()


file_2 = open('ganesha.txt','a')
file_2.write("kdld")
#print(file_2.read())
file_2.close()

file_3 = open('ganeshanku.txt','w')
file_3.write('lkfjasldj')