#Write a Python program to count the number 4 in a given list.

list = [1, 2, 4, 3, 2, 3, 4]
count = 0 
for i in list:
    if i == 4:
        count += 1
print(count)        

#or 

def list_count(list):
    count = 0
    for i in list:
        if i == 4:
            count += 1
    return count

print(list_count(list))