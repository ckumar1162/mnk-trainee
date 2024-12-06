#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# In[3]:


#Convert the tuple into a list, add "orange", and convert it back into a tuple:
x = ("apple", "banana", "cherry")
y = list(x)
x=y.append("orange")
x=tuple(y)
print(x)


# In[8]:


#Create a new tuple with the value "orange", and add that tuple:
x = ("apple", "banana", "cherry")
y= ("orange",)
z=x+y
print(z)


# In[9]:


#unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


# In[10]:


#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# In[11]:


#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# In[13]:


tuple=4,3,5,6
print(tuple)
t=5,
print(t)


# In[18]:


print(tuple+(9,))
print(tuple+(5,6,7)+tuple)


# In[19]:


tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
''.join(tup)


# In[24]:


#program to create the colon of a tuple.
from copy import deepcopy
tuplex =("HELLO", 5, [], True)
print(tuplex)
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2] .append(50)
print(tuplex_colon)


# In[28]:


tuple=tuple+(3,4,5,2,1,2)


# In[29]:


tuple.count(2)


# In[34]:


#converting tuple to dic
tuplex = ((2, "w"), (3, "r"))
dic=dict((x,y)for x,y in tuplex)
print(dic)


# In[39]:


# program to unzip a list of tuples into individual lists.
l = [(1, 2), (3, 4), (8, 9)]
list(zip(*l))


# In[50]:


t = (100, 200, 300)

# Use the 'format' method to insert the tuple 't' into the string and print the result
print('This is a tuple {0}'.format(t))


# In[56]:


# program to replace the last value of tuples in a list.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l]) 


# In[69]:


#program to remove an empty tuple(s) from a list of tuples.
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
[t for t in L if t]


# In[84]:


import builtins

# Use the built-in tuple explicitly in case it's shadowed
string_tuple = ('1', '2', '3', '4')
integer_tuple = builtins.tuple(map(int, string_tuple))

print("Original tuple of strings:", string_tuple)
print("Converted tuple of integers:", integer_tuple)


# In[3]:


#SET
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


# In[4]:


thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)


# In[5]:


color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set) 


# In[6]:


print("Check if a set is a subset of another set, using comparison operators and issubset():\n")
setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = set(["mango"])
print("x: ", setx)
print("y: ", sety)
print("z: ", setz, "\n")

print("If x is a subset of y")
print(setx <= sety)
print(setx.issubset(sety))

print("If y is a subset of x")
print(sety <= setx)
print(sety.issubset(setx))

print("\nIf y is a subset of z")
print(sety <= setz)
print(sety.issubset(setz))

print("If z is a subset of y")
print(setz <= sety)
print(setz.issubset(sety)) 


# In[ ]:




