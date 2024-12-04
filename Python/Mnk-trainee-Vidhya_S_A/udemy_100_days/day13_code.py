# debugging
words_per_page = 0
pages = int(input("Enter no.of pages:"))
words_per_pages = int(input("ENter no.of words per page:"))
total_words = pages * words_per_pages
print(total_words)

# debug odd or even program
# def odd_or_even(number):
#     if number % 2 = 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."

def odd_or_even(number):
    if number % 2 ==0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."
    
print(odd_or_even(5))    


# leapyear debugging
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(2000))


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:     #The condition year % 4000 == 0 is unnecessary and does not align with the leap year rules.
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(2000))

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 or number % 5 == 0:
            print("FizzBuzz")
        if number % 3 == 0:
            print("Fizz")
        if number % 5 == 0:
            print("Buzz")
        else:
            print([number])


def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])
fizz_buzz(6)                        
