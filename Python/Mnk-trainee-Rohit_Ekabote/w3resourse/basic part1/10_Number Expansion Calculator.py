'''Write a Pytho2 program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615'''

n = 5
n1 = int(str(n) + str(n))
n2 = int(str(n) + str(n) + str(n))
print(n + n1 + n2)

#or

a = int(input("Input an integer: "))

n1 = int("%s" % a)         
n2 = int("%s%s" % (a, a))   
n3 = int("%s%s%s" % (a, a, a)) 

print(n1 + n2 + n3)
