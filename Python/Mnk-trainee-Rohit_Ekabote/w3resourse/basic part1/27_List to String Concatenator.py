#Write a Python program that concatenates all elements in a list into a string and returns it.

list=['h', 'e', 'l', 'l', 'o']
result = ''
for i in list:
    result += i
print(result)

#or

def concatenate_list_data(lst):
    result = ''  
    for element in lst:
        result += str(element) 
    return result 
print(concatenate_list_data([1, 5, 12, 2]))
