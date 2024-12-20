# write python function to rearrange a string in sorted order of alphabets followed by sum of the integers , input : "dacsb4321" and output: "abcds10"

input = "dacsb4321"
def sort_func(x):
    alphabet = ""
    num = 0
    for i in x:
        if i.isalpha():
            alphabet+=i
            
        elif i.isdigit():
            num +=int(i)

    new_str = sorted(alphabet)
    print(''.join(new_str)+ str(num))   
           

            

sort_func(input)