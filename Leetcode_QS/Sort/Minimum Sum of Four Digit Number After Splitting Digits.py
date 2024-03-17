# You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

# For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
# Return the minimum possible sum of new1 and new2.

# Example 1:
# Input: num = 2932
# Output: 52
# Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
# The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
# 1000 <= num <= 9999


#Solution with sort functions
# class Solution:
#     def minimumSum(self, num: int) -> int:
#         l=[]
#         while num!=0:
#             l.append(num%10)
#             num=num//10
#         l.sort()
#         sum=(l[0]*10 +l[3])+(l[1]*10+l[2])
#         return sum
    
#Solution without sort function(trying with bubble sort)
import time

class Solution:
    def minimumSum(self, num: int) -> int:
        l = []
        while num != 0:
            l.append(num % 10)
            num = num // 10

        def timer(func):
            def wrapper_func(*args, **kwargs):
                t = time.time()
                result = func(*args, **kwargs)
                print("Time taken by {} is {} seconds.".format(func.__name__, time.time() - t))
                return result
            return wrapper_func

        @timer
        def bubble_sort(arr):
            n = len(arr)
            for i in range(n):
                for j in range(n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        bubble_sort(l)
        sum_val = (l[0] * 10 + l[3]) + (l[1] * 10 + l[2])
        return sum_val

sol = Solution()
num = 2932
print(sol.minimumSum(num))