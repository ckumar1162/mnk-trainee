from wsgiref.util import request_uri

l=[10,40,50,20]
print(l)

print(sum(l))
# find sum of list items without using build-in function
def sum(items):
    sum=0
    for i in items:
        sum+=i
    return sum
print(sum(l))

# find maximum number from list
def max_num(items):
    maxi=items[0]
    for i in items:
        if i >maxi:
            maxi=i
    return maxi
print(max(l))

# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
li=["abc","xyzx","xyx","abca"]
def count_len(items):
    count=0
    for i in items:
        if len(items)>1 and i[0]==i[-1]:
            count+=1
    return count
print(count_len(li))

# list of tuples will be sorted based on first element in tuple
ll=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
ll.sort()
print(ll)

# sort list of tuples based on 2nd element
l1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def last(n):
    return n[-1]
# use sorted method to sort list of tuples and key arguments takes last element from last function
def l_last(items):
    return sorted(items,key=last)
print("sorted based on last element:",l_last(l1))

# remove duplicate items from a list by converting to set and back to list
l=[1,2,3,2,1]
s=set(l)
l1=list(s)
print(l1)

# remove duplicates from list using loop
l=[1,2,3,2,1,4,5]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)





