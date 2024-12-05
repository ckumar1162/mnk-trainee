s={'hi',"apple","banana","Orange"}
print(type(s))

#s.update("hello")
s1={"google", "microsoft", "apple"}
newset=s.union(s1)
print(newset)

t=("hiii","hello")
ns=s.union(t)
print(ns)

#add items
s1={'hi',"apple","banana","Orange"}
t1=(1,2,3)
s1.update(t1)
print(s1)

s1={'hi',"apple","banana","Orange"}
s.add("staryberry")
print(s)

# remove items
s1={'hi',"apple","banana","Orange"}
r=s1.pop()
print(r)
print(s1)
s1.remove("banana")
print(s1)

s1.discard("Orange")
print(s1)


#add multiple set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
t=("hiii","hello")
newset=set1.union(set2,set3,set4,t)
newset1=set1 | set2 | set3| set4
print(newset1)
print(newset)

# intersection
set1 = {"a", "b", "c",0,True}
set2 = {1, 2, 3,"a"}
n=set1.intersection(set2)
ns=set1 & set2
set1.intersection_update(set2)
print(n)
print(set1)

# difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

ns=set1.difference(set2)
print(ns)
nss= set1 - set2
print(nss)
set1.difference_update(set2)
print(set1)


#Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
ns=set1.symmetric_difference(set2)
nss=set1 ^ set2
print(nss)
set1.symmetric_difference_update(set2)
print(set1)
print(ns)

#Methods
st1 = {"apple", "banana", "cherry"}
st2 = {"apple", "banana", "cherry"}
s3={1,2,3}
sb=st1.issubset(st2)
print(sb)
ss=st1.isdisjoint(st2)
print(ss)
t={1,2}
s=st1.isdisjoint(t)
print(s)
s11=st1.copy()
x=st1.pop()
print(x)
print(st1)
print(s11)


