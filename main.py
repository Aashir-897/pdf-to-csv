import camelot

#path of yout pdf directry
tables = camelot.read_pdf('file:///C:/Users/Administrator/Downloads/foo.pdf')


print(tables)

#converstion pdf to excel
tables[0].to_csv('foo.csv')  

# Optionally, inspect the DataFrame
df = tables[0].df
print(df)
