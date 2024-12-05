# Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'

# s=input("enter the string")
def first_last_charc(str):
    dict={}
    for i in str:
        keys=dict.keys()
        print(keys)
        if i in keys:
            dict[i] +=1
        else:
            dict[i]=1
    return dict


    # if len(str)<2:
    #     return 'empty string'
    # else:
    #     return str[0:2]+str[-2:]
print(first_last_charc("weeernr"))

# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

def change(str):
    char=str[0]
    s=str.replace("o","$")

    str=char+s[1:]
    return str

print(change("HelloHowAreYou"))

