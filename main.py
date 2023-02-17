# a={Todo:Write in csv file
import csv
csvfile=open('try.csv','w+',newline='',encoding='utf-8')
csv.reader()
c=csv.writer(csvfile)

c.writerow(['name','addrss','job'])
csv.DictReader()
csv.DictWriter()
the_list=[
    ['alice','prabhudev','florida','chef'],
    ['alice','prabhudev','florida','chef'],
    ['alice','prabhudev','florida','chef'],
['alice','prabhudev','florida','chef'],
['alice','prabhudev','florida','chef']
]
for item in the_list:
    c.writerow(item)
csvfile.close()


import csv
csvfile=open('try2.csv','w',newline='')
c=csv.writer(csvfile)
c.writerow(['Rollno','Name','address','city'])

my_list=[[1,'ram','daman','vapi'],
        [2,'ram','daman','vapi'],
        [3,'ram','daman','vapi'],
        [4,'ram','daman','vapi']
]
for item in my_list:
    c.writerow(item)
csvfile.close()
#
# todo:Import the module.
# Open a file for writing.
# Create a CSV writer object and assign it to a new variable.
# Write the header row into the CSV.
# Write all the other rows into the CSV. Normally this will involve a for-loop.
# Close the file.