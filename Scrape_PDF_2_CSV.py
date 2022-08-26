# DFS - Quick parse for PDF to CSV
# Pulls a table out of a PDF and then writes to a csv
import camelot
tables = camelot.read_pdf('example.pdf', pages='1')
print(tables)
tables.export('example.csv', f='csv', compress=True)
tables[0].to_csv('example.csv')
