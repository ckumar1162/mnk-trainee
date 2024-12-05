from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Table",["Pickachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","water","Fire"])
print(table)
# text alignment of table
print(table.align)
table.align="l"
print(table)
