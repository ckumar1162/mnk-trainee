'''Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java'''

file = input("enter filename \n")
a = file.split('.')
print(f"the extension of the file :{a[-1]}")
print("The extension of the file is : " + repr(a[-1]))