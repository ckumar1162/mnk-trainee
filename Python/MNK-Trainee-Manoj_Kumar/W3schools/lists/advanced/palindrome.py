def is_palindrome(lst):
    return lst == lst[::-1]

print("Is palindrome:", is_palindrome([1, 2, 3, 2, 1]))