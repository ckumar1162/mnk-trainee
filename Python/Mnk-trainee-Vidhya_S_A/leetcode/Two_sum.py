#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def two_sum(list1,target):
    dict1 = {}
    index =0 
    for i in list1:
        result = target - i
        if result in dict1 :
            return [dict1[result] , index]
        dict1[i] = index
        index+=1

        
print(two_sum([2,7,11,15],9)) 
print(two_sum([3,2,4],6)) 
print(two_sum([3,3],6)) 


