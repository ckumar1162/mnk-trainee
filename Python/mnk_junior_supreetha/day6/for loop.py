l=[4,3,7,5,9]
sum=0
for x in l:
    sum+=x
print(sum)

while x<=len(l):
    sum+=l[x]
    x+1
print(sum)

max=l[0]
for x in l:
    if max < x:
      max=x
print(max)

sum=0
for i in range(1,5):
    sum+=i
print(sum)