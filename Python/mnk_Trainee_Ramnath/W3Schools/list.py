lst=["apple",2,"Hi",10.5,"Hello"]
print(lst)
print(type(lst))
print(len(lst))
i = lst.index("Hello")
print(i)
# access list items
print(lst[2])
print(lst[:3])
print(lst[2:])
print(lst[1:4])
print(lst[-2])
print(lst[-3:-1])
if "applE" in lst:
    print("Yes")
else:
    print("NO")
#change list items  
tlist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]    
tlist[2]="greps"
print(tlist)
tlistt = ["apple", "banana", "cherry"]
tlistt[1:2] = ["watermelon", "banana", 3]
print(tlistt)
tlistt[1:3]=["watermelon","banana",3]
print(tlistt)

tlst = ["apple", "banana", "cherry"]
tlst[1:3]="watermelon"
print(tlst)

tlstt = ["apple", "banana", "cherry", "orange"]
tlstt[1:3]=["watermelan"]
print(tlstt)

#insert method
tlistt = ["apple", "banana", "cherry"]
tlistt.insert(2, 10)
tlistt.insert(5, 5)  # ''add items at last if u specify more  index number'''
print(tlistt)
#add list items
tlistt = ["apple", "banana", "cherry"]
t = (10, 20, 30)
l = ["hi", "hello", 50]
tlistt.extend(l)
tlistt.extend(t)
print(tlistt)
#Remove items
tlistt = ["apple", "banana", "cherry",10,20,30]
tlistt.remove("banana")
print(tlistt)
tlistt.pop(1)
print(tlistt)
tlistt.insert(5,"orange")
print(tlistt)
tlistt.pop()
print(tlistt)
dl= ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
dl.clear()
print(dl)
'''d2=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
del d2
print(d2)'''
# looping with short comprehension
d2=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
[print(x)for x in d2]
for x in d2:
    if "a" in x:
      print(x)
newlist=[x for x in d2 if 'o' in x]
print(newlist)

d2=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
nlist=[x for x in d2]
print(nlist)
# remove if apple is present in list
nlistt=[x for x in d2 if x!="apple"]
print(nlistt)
# cahnge it as 'Watermelon' if 'apple' is present in a list
n=[x if x!='apple' else 'Watermelon' for x in d2]
print(n)
# expression in list
d2=["apple", "banana", "Cherry", "Orange", "kiwi", "mango"]
new=[x.upper() for x in d2]
print(new)
n=[x.lower() for x in d2]
print(n)
t = (10, 20, 30)
l = list(t)
print(l)
nl=["hello" for x in l]
print(nl)

#sort
d=[30,20,50,80,10]
d.sort()
print(d)
d.sort(reverse=True)
print(d)
d.reverse()
print(d)
#case sensitive in list
d2=["apple", "banana", "Cherry", "Orange", "kiwi", "mango"]
d2.sort()
print(d2)
d2.sort(key=str.lower)
print(d2)

#Copy list
l=[10,20,30]
l2=l.copy()
print(l2)

listt=list(l)
print(listt)

# join 2 list
l=[10,20,30]
l2=["hi",10,20]
li=l+l2
print(li)

l.extend(l2)
print(l)

for x in l2:
    l.append(x)
print(l)    
"""NOTE:
       1.cannot use sort() function if a list has string and int type items together
       2.it shows error ,TypeError: '<' not supported between instances of 'int' and 'str'
"""
d2=["apple", "banana", "Cherry", "Orange", "kiwi", "mango"]
d2.sort()
print(d2)

