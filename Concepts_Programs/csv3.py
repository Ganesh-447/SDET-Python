import csv

temp_data=[]
age=26
id_update=2

with open('Testdata.csv','r') as file:
    read = csv.reader(file)
    for row in read:
        temp_data.append(row)

    for i in temp_data:
        if i[0] == id_update:
            i[2]= age

