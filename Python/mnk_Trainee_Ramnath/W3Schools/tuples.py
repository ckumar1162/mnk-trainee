fruits = ("apple", "banana", "cherry")
t=(10,20,"orznge","spple",10.5,True)
print(t)
t1=fruits+t
print(t1)

f=("hi",)
f1=fruits + f
print(f1)

# tuple constructor
nt=tuple(("orange","apple",10,20,True,0))
print(nt)
# access tuple
t = ("apple", "banana", "cherry")
print(t[1])
print(t[:2])
print(t[1:])
print(t[-3:-1])

if "banana" in t:
    print('Yes,its present in tuple')

#Update tuple values
    #add items
t = ("apple", "banana", "cherry")
l=list(t)
l[0]="Orange"
print(l)
t=tuple(l)
print(t)

#remove items
t = ("apple", "banana", "cherry",10)
print(t)
l=list(t)
l.remove(10)
t=tuple(l)
print(t)

''' t = ("apple", "banana", "cherry",10)
 del t
print(t)'''

#Unpack tuple

fr = ("apple", "banana", "cherry",10,40,90)

(green, red,*yellow,num) = fr

print(green)
print(red)
print(yellow)
print(num)

#Loop Tuples
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)
for x in range(len(fruits)):
    print(x)  # '''Print only index  number '''
    print(fruits[x]) #print value

# JOIN 2 tuples using + operator
fruits = ("apple", "banana", "cherry")
t=(10,20,"orznge","spple",10.5,True)
t1=fruits+t
print(t1)

#multiply tuples
fs= ("apple", "banana", "cherry")
f=fs * 3
print(f)

# Methods in tuple
fs= ("apple", "banana", "cherry","apple")
c=fs.count("apple")
print(c)
i=fs.index("cherry")
print(i)


