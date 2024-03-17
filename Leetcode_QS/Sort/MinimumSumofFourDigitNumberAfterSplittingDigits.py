# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/


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