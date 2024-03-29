#Question :Two sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]. 
# Refer:https://www.linkedin.com/pulse/exploring-two-sum-problem-two-pointer-approach-jean-claude-adjanohoun-xjn6c/





def twosum(arr,target):
    # Taking two pointer i and iterate through each element
    n=len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # Start from i + 1 to avoid comparing the same element
            if arr[i] + arr[j] == target:
                return [i, j]
    return [] 

arr=[2,7,11,15]
target=9
print(twosum(arr,target))

                
#solution:
# 1.Sort the array if it is not sorted .This is an essential step
# 2.initialize two pointers
# 3.iterate and find the pairs 
# 4.repeate until a solution is ofund and return the result
