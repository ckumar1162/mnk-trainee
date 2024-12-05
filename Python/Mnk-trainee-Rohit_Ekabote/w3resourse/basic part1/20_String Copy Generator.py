#Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
user =  str(input("enter the string : "))
copies = int(input("enter the number of copies you want: "))
result = ''
for i in range(copies):
    result += user
print(result)

#or
def repeat(user, copies):
    result = ''
    for i in range(copies):
        result += user
    return result
print(repeat(user, copies))