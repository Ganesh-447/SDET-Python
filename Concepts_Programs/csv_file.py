import csv


with open('Testdata.csv','r') as csvfile:
    read = csv.reader(csvfile)
    for row in read:
        #print(row)
        print(' '.join(row))


