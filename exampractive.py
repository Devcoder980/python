# import csv
# csvfile=open('stocks.csv','w+')
# a=csv.writer(csvfile)
# a.writerow(['name','addres','job'])
# csvfile.close()
string1="editing"
string2="distance"
L1 = length(string1)
L2 = length(string2)
for i in L1:
    table[i][0] = i
for i in L2:
    table[0][i] = i
for i in L1:
    for j in L2:
        m = minimum(table[i-1][j],table[i][j-1])+1
        if s[i] == t[j]: subvalue = 1
        else: subvalue = 0
        table[i][j] = minimum(m, table[i-1][j-1] + subvalue)
return table[L1][L2]