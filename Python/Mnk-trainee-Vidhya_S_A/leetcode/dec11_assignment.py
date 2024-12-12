# Assignment for Wednesday (11 Dec)
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# nums = [2,2,1]
# Output: 1

# nums = [4,1,2,1,2]
# Output: 4

# nums = [1]
# Output: 1


def single_element(list1):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
        elif i in result:
            result.remove(i)    
    return result

print(single_element([2,2,1]))  
print(single_element([4,1,2,1,2]))
print(single_element([1]))
print(single_element([1,2,3,3,4,5,4,5]))           





    