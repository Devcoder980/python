
n=int(input("Enter How many value input:"))
for i in range(n):
    import pandas as pd
    pname=input("Enter Product Name:")
    a=int(input("Enter March Sales:"))
    b=int(input("Enter april Sales:"))
    c=int(input("Enter may Sales:"))
    d=int(input("Enter june Sales:"))
    e=int(input("Enter july Sales:"))
    list=[a,b,c,d,e]
    totalsale=a+b+c+d+e
    averageales=(a+b+c+d+e)/5
    list.sort()
    min=list[0]
    max=list[-1]

    data={'Productname':[f'{pname}'],

    'march':[f'{a}'],
    'april':[f'{b}'],
    'may':[f'{c}'],
    'june':[f'{d}'],
    'july':[f'{e}'],
    'Totalsale':[f'{totalsale}'],
    'Average':[f'{averageales}'],
    'Max':[f'{max}'],
    'Min':[f'{min}']
    }
    df=pd.DataFrame(data)
    df.to_csv('sales.csv', mode='a', index=False, header=False)
    print(df.values)
    dff=pd.read_csv('sales.csv')
    dff.to_excel('the.xlsx',sheet_name='sheet2',index=False)
    print(dff.values)


