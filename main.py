# pip install camelot-py
# pip install gs
import camelot

# The path where you want to export pdf file
tables = camelot.read_pdf('file:///C:/Users/Administrator/Downloads/foo.pdf')


print(tables)

# Converting a Table pdf to csv
tables[0].to_csv('foo.csv')  


df = tables[0].df
print(df)
