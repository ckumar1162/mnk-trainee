#Write a Python program to test whether a passed letter is a vowel or not.

vowel = 'aeoiuAEIOU'
user = str(input('enter the letter: '))
if user in vowel:
    print("vowel")
else:
    print('not')
    
#or 
def check_vowel(letter):
    return letter in vowel
print(check_vowel(user))