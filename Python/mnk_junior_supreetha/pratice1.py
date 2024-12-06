#!/usr/bin/env python
# coding: utf-8

# In[2]:


height=int(input("enter the height:"))
age=int(input("enter the age:"))
bill=0
if height>=120:
    print("can ride")
    if age<12:
        bill=5
        print("$5")
    elif age>12 and age<18:
        bill=7
        print("$7")
    elif age>=45 and age<=55:
        print("$0")    
    else:
        bill=12
        print("$12")
    photos=input("do u need photos:")
    if photos=='yes':
        print("+$3")
    bill+=3
    print("total bill:",bill)

else:
    print("cant ride")


# In[1]:


print("welcome to python Pizza Deliveries!")
size=input("what size pizza do u want? S, M or L:")
bill=0
if size=='S':
    bill+=15
    pepperoni=input("do you want pepperoni on pizza? Y or N:")
    if pepperoni=='Y':
        bill+=2
elif size=='M':
    bill+=20
    pepperoni=input("do you want pepperoni on pizza? Y or N:")
    if pepperoni=='Y':
        bill+=3
else:
    bill=25
    pepperoni=input("do you want pepperoni on pizza? Y or N:")
    if pepperoni=='Y':
        bill+=3
cheese=print(input("do u need extra cheese? Y or N:"))
bill+=1
print("your total bill is:",bill)
        


# In[16]:


import random
value=random.randint(0,1)
if value==1:
    print("head")
else:
    print("tail")


# In[19]:


import random
#import my_module

random_integer=random.randint(1,10)
print(random_integer)
#print(my_module.my_fav_number)

random_float=random.random()
print(random_float)

random_floatrange=random.uniform(1,10)
print(random_floatrange)

value=random.randint(0,1)
if value==0:
    print("head")
else:
    print("tail")


# In[10]:


import random
friends=['Alica','Bob','Charlie','David']
print(random.choice(friends))

random_index=random.randint(0,3)
print(friends[random_index])





# In[2]:


import random
letters=['a','b','c','d','e','f']
numbers=['0','1','2','3','4','5']
symbols=['!','#','$','%']

print("welcome to pypassword Generator!")
ltr=int(input("how many letters u like to add:\n"))
no=int(input("how many no u like to add\n"))
spl=int(input("how many spl u like to add\n"))
l1=random.sample(letters,ltr)
l2=random.sample(numbers,no)
l3=random.sample(symbols,spl)

l=[]

l.extend(l1)
l.extend(l2)
l.extend(l3)
random.shuffle(l)

l4=" ".join(l)
print(l4)


# In[ ]:





# In[ ]:


import random
word_list=['aardvark','baboon','camel']
choice=random.choice(word_list)
print(choice)
placeholder=" "
rchoice=len(choice)
for x in range(rchoice):
    placeholder+="_" 
print(placeholder)
    
game_over=False
correct_letters=[]
lives=6

while not game_over :   
    guess=input("guees the letter:").lower()
    print(guess)

    display=" "
    for letter in choice:
        if letter==guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter

        else:
            display+="_"
    print(display)
    
   
    if guess not in choice:
        lives-=1
        if lives==0:
            gameover=True
            print("You lose")
    if "_" not in display:
        game_over=True
        print("you win")
     


# In[1]:


import random

# List of words to choose from
word_list = ['aardvark', 'baboon', 'camel']
choice = random.choice(word_list)
print("Pssst, the word is:", choice)  # Cheat code for testing

# Placeholder for the word with blanks
display = "_" * len(choice)
print(display)

# Game variables
game_over = False
lives = 6
correct_letters = []

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")

    # Update display for correct guesses
    new_display = ""
    for i in range(len(choice)):
        if choice[i] == guess:
            new_display += guess
        else:
            new_display += display[i]
    display = new_display

    # Check if the guess is wrong
    if guess not in choice:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives remaining.")
        if lives == 0:
            game_over = True
            print("You lose! The word was:", choice)
    else:
        print("Correct guess!")
          # Display current progress
    print(display)

    # Check if the player has won
    if "_" not in display:
        game_over = True
        print("You win!")

# End of the game
print("Game over.")



# In[3]:


import sys
# Use the sys.version attribute to get the Python version and print it
print(sys.version)


# In[7]:


import datetime
print(datetime.datetime.now())


# In[13]:


from math import pi
r=float(input("enter radius of the circle:"))
area=pi*r**2
print("area of the circle with radius" + str(r) + 'is:' + str(area))


# In[22]:


#Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them
name=input("enter your first and last name:")
name1=name.split(" ")
name2=name1[::-1]
name3=' '.join(name2)
print(name3)


# In[25]:


#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates
#a list and a tuple of those numbers.
str=3,4,2,6
print(list(str))
print(tuple(str))


# In[2]:


#to print extention of file name
file=input("enter a file name:")
file1=file.split('.')
print(file1[-1])


# In[3]:


#Create a list called 'color_list' containing color names and display 1st and lst colour
color_list = ["Red", "Green", "White", "Black"]
print(color_list[0],color_list[-1])


# In[9]:


exam_st_date = (11, 12, 2014)
a=str(exam_st_date )
# Print the exam start date using string formatting
# The '%i' placeholders are filled with the values from the 'exam_st_date' tuple
print("The examination will start from : %i / %i / %i" % exam_st_date)
print(a.replace(',','/'))


# In[11]:


a=input('enter a number:')
n1=int(a)
n2=int(a+a)
n3=int(a+a+a)
print(n1+n2+n3)


# In[1]:


def greet():
    print("hi")
    print("hello")
    print('abc')
greet()


# In[5]:


def greet_with(name,location):
    print(f"hello {name}")
    print(f"what is it in {location}")
greet_with("supi","tmk")
greet_with(name="supi",location='tmk')
greet_with(name="tmk",location='supi')


# In[8]:


age=input("what is your current age:")
age_int=int(age)

years_remaining=90-age_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
print(f"you have years {years_remaining},months {months_remaining},weeks{weeks_remaining},days {days_remaining}")



# In[3]:


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
direction=input("type 'encode' to encrypt,type 'decode', to decrypt:\n").lower()
text=input("type your message:\n").lower()
shift=int(input("type the shift number:\n"))
def caesar(original_text,shift_amount,encode_or_decode):
    output_text=" "
    for letter in original_text:
        if encode_or_decode=="decode":
            shift_amount*= -1
        shifted_position=alphabet.index(letter)+shift_amount
        shifted_position %=len(alphabet)# so that it wont cross the limit 
        output_text+=alphabet[shifted_position]
    print(f"here is the {encode_or_decode}result:{output_text}")
caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    


# In[ ]:


alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']

def caesar(original_text,shift_amount,encode_or_decode):
    output_text=" "
    if encode_or_decode=="decode":
                shift_amount*= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            
            shifted_position=alphabet.index(letter)+shift_amount
            shifted_position %=len(alphabet)# so that it wont cross the limit 
            output_text+=alphabet[shifted_position]
    print(f"here is the {encode_or_decode}result:{output_text}")

should_continue=True

while should_continue:
    direction=input("type 'encode' to encrypt,type 'decode', to decrypt:\n").lower()
    text=input("type your message:\n").lower()
    shift=int(input("type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart=input("type 'yes',if you want to go again.otherwise,type'no'.\n").lower()
    if restart=='no':
        should_continue==False
        print("goodbye")


# In[2]:


l=[1,3,4]
print(len(l).__doc__)


# In[3]:


# Print the calendar for the specified year and month
import calendar

y = int(input("Input the year : "))
m = int(input("Input the month : "))

# Print the calendar for the specified year and month
print(calendar.month(y, m))


# In[4]:


# Use triple double-quotes to create a multi-line string
print(""" string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")


# In[7]:


#program to calculate the number of days between two dates.
from datetime import date
lstdate=date(2001,7,10)
newdate=date(2024,11,19)
delta=newdate-lstdate
print(delta.days)


# In[8]:


#program to get the volume of a sphere with radius six.
pi = 3.1415926535897931
r = 6.0
V = 4.0/3.0 * pi * r**3
print('The volume of the sphere is: ', V)



# In[13]:


# program to calculate the difference between a given number and 17. If the number is greater than 17, 
#return twice the absolute difference
num1=int(input("enter a number:"))
num2=17
num=num1-num2
if num1>17:
    print(num*2)
else:
    print(abs(num))


# In[15]:


#program to test whether a number 
#is within 100 of 1000 or 2000.
def near_thousand(n):
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(500))
print(near_thousand(900))


# In[24]:


#Write a Python program to calculate the sum of three given numbers.
#If the values are equal, return three times their sum.
def sum(n1,n2,n3):
    sum1=n1+n2+n3
    if n1==n2==n3:
        print(sum1*3)
    else:
        print(sum1)
sum(3,2,3)
sum(3,3,3)


# In[27]:


#program to get a newly-generated string from a given string where "Is" has been added to the front. 
#Return the string unchanged if the given string already begins with "Is".
def string(a):
    if a[:2]=='if':
        print(a)
    else:
        added='if' +a
        print(added)
        
string('supi')
        


# In[31]:


#program that returns a string that is n (non-negative integer) copies of a given string.
def copy(string,num):
    result=''
    for i in range(3):
        result+=string
    print(result)
        
copy('supi',3)


# In[32]:


#odd or even
def number(a):
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
number(3)


# In[38]:


#program to count the number 4 in a given list
count=0
l=[2,4,3,6,4,9,4]
for i in l:
    if i==4:
        count+=1
print(count )     


# In[44]:


#program to get n (non-negative integer) copies of the first 2 characters of a given string. 
#Return n copies of the whole string if the length is less than 2.
def copies(string,number):
   if len(string)>2 :
       print(string[:2]*number)
   else:
       print(string*number)
copies('supi',2)


# In[5]:


#Write a Python program to test whether a passed letter is a vowel or not.
voweles=['a','e','i','o','u']
def vowel(letter):
    if letter in voweles:
        print(f"{letter}is vowl")
    else:
        print(f"{letter}is not a vowl")
vowel('y')


# In[9]:


#Write a Python program that checks whether a specified value
#is contained within a group of values.
values=[3,6,5,2]
def value(num):
    if num in values:
       # print(f" {num} is present in values")
       return True
value(3)


# In[17]:


#program to create a histogram from a given list of integers.
#items=[2,3,4,5]
def histogram(num):
    for n in num:
        output=''
        times=n
        
        while times>0:
            output+='*'
            times=times-1
        print(output)
histogram([2,3,4,5])


# In[19]:


#Write a Python program to print all even numbers from a given list of numbers in the 
#same order and stop printing any after 237 in the sequence.


numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for x in numbers:
    if x == 237:
        print(x)  # Print the number if it's 237.
        break  # Exit the loop if 237 is found.
    elif x % 2 == 0:
        print(x)
        


# In[20]:


# Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
color=color_list_1-color_list_2 
print(color)


# In[25]:


#program to sum three given integers. However, if two values are equal, the sum will be zero
def sumation(n1,n2,n3):
    if n1==n2 or n2==n3 or n3==n1:
        sum=0
        print(sum)
    else:
        sum=n1+n2+n3
        print(sum)
sumation(3,4,5)
sumation(3,3,5)


# In[30]:


#Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
def sumint(n1,n2):
    sum=n1+n2
    if sum>=15 and sum<20:
        sum=20
        print(sum)
    else:
        print(sum)
sumint(20,5)
sumint(15,3)


# In[32]:


# program that returns true if the two given integer values are equal or their sum or difference is 5.
def sum(n1,n2):
    if n1==n2 or n1+n2==5 or n1-n2==5:
        return True
    else:
        return False
sum(3,2)  
sum(5,6)


# In[34]:


def add_numbers(a, b):
    # Check if both 'a' and 'b' are integers using the 'isinstance' function.
    if not (isinstance(a, int) and isinstance(b, int)):
        # If either 'a' or 'b' is not an integer, return an error message.
        return "Inputs must be integers!"
    # If both 'a' and 'b' are integers, return their sum.
    return a + b
add_numbers(3,4)
add_numbers(5.4,3)


# In[40]:


#program to solve (x + y) * (x + y).
def double(x,y):
    result=(x+y)**2
    print("({} + {}) ^ 2) = {}".format(x, y, result))
double(3,4)
#print("({} + {}) ^ 2) = {}".format(x, y, result))


# In[1]:


#program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
import struct

# Use the 'calcsize' function to determine the size (in bytes) 
print(struct.calcsize("P") * 8)


# In[2]:


import platform
import os
print("Name of the operating system:", os.name)
print("\nName of the OS system:", platform.system())
print("\nVersion of the operating system:", platform.release())


# In[5]:


import os
# Use the 'os.path.realpath(__file__)' to get the full path of the current Python script.
# This will print the path of the current file.
print("Current File Name: ", os.path.realpath('Untitled57'))


# In[9]:


for i in range(0, 10):
    print('*', end="")

print("\n")


# In[6]:


#caluclater program
def add(n1,n2):
    return n1+n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={
           '+':add,
           '-':substract,
           '*':multiply,
           '/':divide,
           }

def caluclate():
    should_accumulate=True

    num1=float(input("enter first number:"))
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operation_symbol=input("pick the operation:")
        num2=float(input("enter second number:"))
        answer=operations[operation_symbol](num1,num2)
        print(f" {num1}{operation_symbol}{num2}={answer}")
        choice=input(f"type 'y'to continue caluclating with{answer},or type 'n' for no")
        if choice=='y':
              num1=answer
        else:
            should_accumulate=False
            print("\n"*20)
    
caluclate()


# In[12]:


#program to count the number of characters (character frequency) in a string.
string1="google.com"
d={}
for x in string1:
    if x  in d.keys():
        d[x]= d[x]+1
    else:
        d[x]=1
print(d)


# In[18]:


#Write a Python program to get a string made of the first 2 and last 2 characters of a given string. 
#If the string length is less than 2,return the empty string instead.
string="supreetha"
#for x in string:
if len(string)>=2:
    print(string[:2],string[-2:])
else:
    print("empty string")


# In[34]:


#program to get a string from a given string where all occurrences of its first char have been changed to '$', 
#except the first char itself.
def check(char):
    str1=char[0]
    string=char.replace(str1,'$')
    done=str1+string[1:]
    print(done)
check('restart')    


# In[40]:


#program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.
def string(a,b):
    n1= b[:2]+a[2:]
    n2=a[:2]+a[2:]
    c=n1+ ' '+n2
    print(c)
string('abc','xyz')


# In[46]:


#program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3,
#leave it unchanged.

def add(a):
    if len(a)>=3  and a[-3:]=='ing':
        print(a+'ly')
    elif len(a)>=3 :
        print(a+'ing')
    else:
        print("len is less then 3")
add("writing")


# In[3]:


# modifing globel var using return 
enemies=1
def increase_enemies(enemy):
    print(f"enemies inside function:{enemies}")
    return enemy+1
enemies=increase_enemies(enemies)

print(f"enemies outside function:{enemies}")


# In[1]:


number=10
print("Welcome to number Guessing Game!")
print("I,am thinking of a number between 1 and 100")
choice=input("chosse a difficulty.Type 'easy' or 'hard':")
print(choice)
if choice=='easy':
    a=10
elif choice=='hard':
    a=5
else:
    print("invalid input")
    guess=input("Make a guess:")
    
while a>=1:
    print(f"you have {a} attempts remaining to guess the number")
    guess=int(input("Take a guess:"))
    if guess==number:
        print("correct guess")
        break
    elif guess>number:
        print("To high")
    else:
        print("To low")
    a-=1
if a==0:
    print(f"your out of attempts.the number was{number}")
    


# In[2]:


import random
import math
def mutate(a_list):
    b_list=[]
    new_item=0
    for item in a_list:
        new_item=item*2
        new_item+=random.randint(1,3)
        new_item=new_item+item
    b_list.append(new_item)1
    print(b_list)
    
mutate([2,4,5,6])


# In[2]:


# program to convert JSON data to Python object.
import json
json_obj = ' { "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 


# In[10]:


#Write a Python program to convert Python object to JSON data.
import json
python_obj =  { "Name":"David", "Class":"I", "Age":6 }
json_obj = json.dumps(python_obj)
print("\nJSON data:")
print(json_obj)


# In[11]:


#program to convert Python objects into JSON strings. Print all the values
import json
python_dict =  {"name": "David", "age": 6, "class":"I"}
python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)

json_dict = json.dumps(python_dict)
json_list = json.dumps(python_list)
json_str = json.dumps(python_str)
json_num1 = json.dumps(python_int)
json_num2 = json.dumps(python_float)
json_t = json.dumps(python_T)
json_f = json.dumps(python_F)
json_n = json.dumps(python_N)

print("json dict : ", json_dict)
print("jason list : ", json_list)
print("json string : ", json_str)
print("json number1 : ", json_num1)
print("json number2 : ", json_num2)
print("json true : ", json_t)
print("json false : ", json_f)
print("json null ; ", json_n)


# In[12]:


#program to convert Python dictionary object (sort by key) to JSON data. 
#Print the object members with indent level 4.
import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))


# In[13]:


#program to convert JSON encoded data into Python objects.
import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'
python_dict =  json.loads(jobj_dict)
python_list = json.loads(jobj_list)
python_str =  json.loads(jobj_string)
python_int =   json.loads(jobj_int)
python_float = json.loads(jobj_float)

print("Python dictionary: ", python_dict)
print("Python list: ", python_list)
print("Python string: ", python_str)
print("Python integer: ", python_int)
print("Python float: ", python_float)


# In[15]:


#Write a Python program to access only unique key value of a Python object.
import json
python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(type(python_obj))
print(python_obj)
json_obj = json.loads(python_obj) # in dic only unique key should be there so while parsing takes last key
print("\nUnique Key in a JSON object:")
print(json_obj) 


# In[3]:


import turtle as t
import random
tim=t.Turtle()

def draw_shape(num_side):
    angle=360/num_side
    for _ in range(num_side):
        tim.forward(100)
        tim.right(angle)
for shape_side in  range(3,11):
    #tim.color(random.change)
    draw_shape(shape_side)
    


# In[ ]:




