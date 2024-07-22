from bs4 import BeautifulSoup
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

cat=BeautifulSoup(html,"html.parser")
table_bs = BeautifulSoup(table, "html.parser")
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

tag_object=cat.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))
tag_object=cat.h3
print(tag_object)
tag_child=tag_object.b 
print(tag_child)
parent_tag=tag_child.parent
print(parent_tag)
sibling_1=tag_object.next_sibling
print(sibling_1)
sibling_2=sibling_1.next_sibling
print(sibling_2)
print(tag_child["id"])
print(tag_child.attrs)
print(tag_child.get('id'))
print(tag_child.string)
print(type((tag_child.string)))
unicode_string = str(tag_child.string)
print(type(unicode_string))
table_rows=table_bs.find_all('tr')
print(table_rows)
first_row =table_rows[0]
print(first_row)
print(first_row.find_all('td'))
##for i,row in enumerate(table_rows):
    ##print("row",i,"is",row)
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)
list_input=table_bs .find_all(name=["tr", "td"])
print(list_input)
print(table_bs.find_all(id="flight"))
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)
#print(table_bs.find_all(href=True))
print(table_bs.find_all(href=False))
print(cat.find_all(id="boldest"))
print(table_bs.find_all(string="Florida"))
print(two_tables_bs.find("table"))




