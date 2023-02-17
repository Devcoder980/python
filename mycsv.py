import csv
c=open("csv1.csv",'w',newline='')
c1=csv.writer(c)
# c1.writerow(['Abc','23','45','23'])
l=[['Abc','23','45','23'],['Abc','23','45','23'],['Abc','23','45','23'],['Abc','23','45','23']]
for i in l:
    c1.writerow(i)
print("Data Written successfully.....")
c=open('csv1.csv','r')
c1=csv.reader(c)
for row in c1:
    print(row)
c.close()