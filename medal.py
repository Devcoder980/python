# .mode csv
# .import a.csv medal
# .mode table
# select * from medal;

import pandas as pd
import sqlite3
con=sqlite3.connect('stockdata2.db')
cur=con.cursor()
import matplotlib.pyplot as plt
cur.execute('select count(*) from medalss;')
cur.execute('select * from medalss where gold >30;')
a=cur.fetchall()
print(a)
df=pd.read_csv('a.csv')

print(df.shape)

print(df.dtypes)

print(df.info())

x = df['total_medal']
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='orange', alpha=1)
plt.show()
plt.show()
con.close()