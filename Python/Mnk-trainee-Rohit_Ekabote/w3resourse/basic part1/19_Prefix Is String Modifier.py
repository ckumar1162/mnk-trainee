'''Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
Return the string unchanged if the given string already begins with "Is".'''

string = str(input("enter you string: "))
if len(string) > 2 and string[:2] == 'Is':
    print(string)
else:
    print('Is' + string)
    
#or
    
def check_string(string):
    if len(string)>2 and string[0:2] == 'Is':
        return string
    else:
        return 'Is' + string
    