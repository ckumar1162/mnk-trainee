#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()


# In[2]:


my_dict = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 3}

# Sorting in ascending order by value
ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Sorting in descending order by value
descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# Displaying results
print("Original Dictionary:", my_dict)
print("Ascending Order:", ascending)
print("Descending Order:", descending)


# In[5]:


# Python program to add a key to a dictionary.
d = {0: 10, 1: 20}
print(d)
d[2]=30
print(d)
d.update({4:40,5:50})
print(d)


# In[6]:


#Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={}
for i in (dic1,dic2,dic3):
    dic4.update(i)
print(dic4)


# In[8]:


#Python script to check whether a given key already exists in a dictionary.
d
d[1]


# In[10]:


for x , y in d.items():
    print({x,y})


# In[11]:


{x:x*x for x in range(16)}


# In[12]:


result=sum (d.values())
print(result)


# In[17]:


result=1
for x in d:
    result=result*d[x]
print(result)


# In[1]:


x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}
item=set(x.items()) & set(y.items())
print(item)


# In[1]:


dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dict={}
for (key, value) in dict1.items() :
    if value is not None:
        dict[key]=value
        
print(dict)


# In[3]:


s='supreetha'
d={}
for x in s:
    if x in d.keys():
        d[x]+=1
    else:
        d[x]=1
print(d)


# In[4]:


from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('\nMember name: {}'.format(Country.Albania.name))
print('Member value: {}'.format(Country.Albania.value))


# In[6]:


from enum import Enum
class Country(Enum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
for data in Country:
    print('{:15} = {}'.format(data.name, data.value))


# In[9]:


import enum
class Country(enum.IntEnum):
    Afghanistan = 93
    Albania = 355
    Algeria = 213
    Andorra = 376
    Angola = 244
    Antarctica = 672
print('Country Name ordered by Country Code:')
print('\n'.join('  ' + c.name for c in sorted(Country)))


# In[11]:


# program to find the most common elements and their counts in a specified text.##
from collections import Counter
s = 'lkseropewdssafsdfafkpwe'
print("Original string: " + s)
print("Most common three characters of the said string:")
print(Counter(s).most_common(3)) 


# In[12]:


#program to find the occurrences of the 10 most common words in a given text.
from collections import Counter
import re

# Define a multi-line text string containing information about Python
text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""

# Use a regular expression to extract words from the text
words = re.findall('\w+', text)
print(Counter(words).most_common(10))


# In[ ]:




