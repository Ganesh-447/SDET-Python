import  csv


a=[['Name','Age','City'],
   ['Ganesh','Sai','Mandy']]


with open('Testdata.csv','a') as file:
    write = csv.writer(file)

    for i in a:
        write.writerow(a)