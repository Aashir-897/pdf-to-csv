import camelot


tables = camelot.read_pdf('file:///C:/Users/Administrator/Downloads/foo.pdf')


print(tables)

# Export the first table to a CSV file
tables[0].to_csv('foo.csv')  # or export it directly using tables.export()

# Optionally, inspect the DataFrame
df = tables[0].df
print(df)
