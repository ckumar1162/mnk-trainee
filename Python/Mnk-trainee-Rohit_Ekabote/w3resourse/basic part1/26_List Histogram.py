#Write a Python program to create a histogram from a given list of integers.

character =  input("enter the character: ")
list = list(input("enter the formate"))

for i in list:
    result = ''
    for j in range(int(i)):
        result += character
    print(result)

#or 
def histogram(items):
    for n in items:
        output = ''  
        times = n     
        while times > 0:
            output += '*'
            times = times - 1 
        print(output)
histogram([2, 3, 6, 5])