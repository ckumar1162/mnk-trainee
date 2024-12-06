#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
from array import *
array_num= array('i', [1,3,5,7,9])
for x in array_num:
    print(x)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])


# In[9]:


#Python program to append a new item to the end of the array.
Original_array=array('i', [1, 3, 5, 7, 9])
Original_array.append(10)
print(Original_array)


# In[1]:


from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))


# In[10]:


from array import *
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Length in bytes of one array item: "+str(array_num.itemsize))


# In[14]:


#program to get the number of occurrences of a specified element in an array.
array_num = array('i', [1, 3, 5, 7, 9,3])
print("Original array: "+str(array_num))
print("modified array" +str(array_num.count(3)))
   


# In[20]:


#program to append items from inerrable to the end of the array.
array_num = array('i', [1, 3, 5, 7, 9,3])
print("Original array: "+str(array_num))
array_num.extend(array_num)
print(array_num)


# In[21]:


#program to convert an array to an array of machine values and return the bytes representation.
from array import *
print("Bytes to String: ")
x = array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
s = x.tobytes()
print(s)


# In[23]:


Original_array=array('i', [1, 3, 5, 7, 9])
Original_array.insert(1,10)
print(Original_array)


# In[24]:


#program to append items to a specified list.
from array import *
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))


# In[27]:


#Python program to remove a specified item using the index of an array.
Original_array=array('i', [1, 3, 5, 7, 9])
Original_array.remove(5)
print(Original_array)


# In[31]:


#program to remove the first occurrence of a specified element from an array.
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
print("Remove the first occurrence of 3 from the said array:")
array_num.remove(3) # remove will remove only first occurance
print("New array: "+str(array_num))


# In[32]:


from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
num_list = array_num.tolist()
print("Convert the said array to an ordinary list with the same items:")
print(num_list)


# In[ ]:




