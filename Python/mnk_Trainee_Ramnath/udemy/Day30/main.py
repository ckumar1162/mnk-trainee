try:
    file=open('data.txt')
    dic={'key':'value'}
    print(dic['key'])

except FileNotFoundError:
    content=open('data.txt','w')
    content.write('Hii welcome')
except KeyError as msg:
    print(f"The key is {msg} not in dictionary")

# this line execute only when there was no exception in try block
else:
    print('Hello ')

# this line execute if there was no error also
finally:
    file.close()
    print("The file is closed")

# TODO: Raising pur own exception

height=float(input('Height: '))
weight=int(input('weight: '))

if height >3:
    raise TypeError('The Height should not be more than 3 meter')

bmi=weight / height**2
print(bmi)