import csv
# import the module
csvfile=open('sample1.csv',newline='')
# open a file for reading
c=csv.reader(csvfile)
# create a csv reader object and assign new variable

# for loop for read all rows in csv file
for row in c:
    print( row[0] +","+row[1]+","+row[2]+","+row[3]+","+row[4])

# close the file
csvfile.close()