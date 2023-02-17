import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
con = sqlite3.connect('stockdata.db')
cur = con.cursor()
# cur.execute('''create table Stock_data(sid integer primary key AUTOINCREMENT,
#                 name text,
#                  opening_price int ,
#                  current_price int ,
#                  previous_price int ,
#                  Highest int ,
#                  lowest int );''')
print("Table Created Succesfully")
n=int(input("Enter How many value input:"))
# for i in range(n):
#     name=input("Enter Stock Company name:")
#     openp=int(input("Enter Stock Opening Price:"))
#     curp=int(input("Enter Stock Current Price:"))
#     prep=int(input("Enter Stock Previous Price:"))
#     high=int(input("Enter Stock Highest Price:"))
#     low=int(input("Enter Stock Lowest Price:"))
#     cur.execute(f'''insert into stock_data(name,opening_price,
#                 current_price,previous_price,highest,lowest) values('{name}',{openp},{curp},{prep},{high},{low});''')
#     con.commit()

# cur.execute("select * from stock_data;")
# print(cur.fetchall())

# cur.execute('alter table stock_data add column daychange int;')
# cur.execute("update stock_data set daychange=opening_price-current_price; ")
#
# cur.execute('alter table stock_data add column avg int;')
# cur.execute("update stock_data set avg=(Highest+lowest)/2; ")
# con.commit()

df=pd.read_csv('stock.csv')
plt.plot(df['sid'],df['current_price'])
plt.title("Stock")
plt.show()
plt.bar(df['sid'],df['Highest'],color="Green")
plt.xlabel("SID no ->")
plt.legend("Highest")
plt.show()
plt.plot(df['sid'],df['lowest'],color="red")
plt.legend("lowest")
plt.ylabel("NO ov vlaues->")
plt.show()

plt.plot(df['sid'],df['avg'],color="yellow")
plt.legend("Average")
plt.ylabel("NO ov vlaues->")
plt.show()


plt.bar(df['sid'],df['daychange'],color="yellow")
plt.title("DayChange")
plt.legend("Daychange")
plt.ylabel("NO ov vlaues->")
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(df['sid'],df['current_price'])
axs[0,1].plot(df['sid'],df['opening_price'])
axs[1,0].plot(df['sid'],df['previous_price'])
axs[1,1].plot(df['sid'],df['Highest'])
plt.show()
a=df.values
df=pd.DataFrame(a)
df.to_excel("values.xlsx")
# con.commit()
print("succesful")
# con.close()
