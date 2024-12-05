d ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(d)
x=d.keys()
y=d.values()
print(x)
print(y)
#access items
print(d['model'])
z=d.get("year")
print(z)
# change items
d['year']=1998
print(d)
d.update({'year':2000})
print(d)
# add items
d1={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
d1["color"] = "blue"
print(d1)

d1.update({'seats':"2 seats"})
print(d1)

#remove items
d1={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

d1['color']='blue'
#d1.pop('year')
#d1.popitem()
#del d1
d1.clear()
print(d1)

#loop dic
d={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in d:
    print(x)
for x in d:
    print(d[x])
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x,y in d.items():
    print(x,y)
# copy dic
nd=d.copy()
print(nd)
#nested dictionary
names={
    "n1":{"name":"ramnath","age":25},"n2":{"name":"Sharanya","age":26},"n3":{"name":"pavan","age":24}}
print(names)
print(names['n1'])
print(names['n2']['age'])

child1={'name':'Ram','year':1999}
child2={'name':"sharanya",'year':1995}
child3={'name':'Pavan','year':2000}

childnames={'c1':child1,'c2':child2,'c3':child3}
print(childnames)
# loop through nested dic
for x,obj in names.items():
    print(x)
    for y in obj:
        print(y + ':',obj[y])
