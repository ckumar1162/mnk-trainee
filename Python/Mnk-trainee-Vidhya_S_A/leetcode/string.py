#Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for too long, resulting in a character being typed multiple times.

# Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

# You are given a string word, which represents the final output displayed on Alice's screen.

# Return the total number of possible original strings that Alice might have intended to type


def og_string(word):
    new = set()
    i = 0 
    n = len(word)
    while i < n:
        j = i
        while j < n and word[j] == word[i]:
            j+=1

        for letter in range(1,j-i+1):
            new_word = word[:i] + word[letter +1:]
            new.add(new_word) 
        i = j      
    print(new)        
    return len(new)
    

print(og_string("abbcccc"))  
print(og_string("abcd")) 
print(og_string("aaaa"))      