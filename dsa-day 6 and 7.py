#!/usr/bin/env python
# coding: utf-8

# In[2]:


# QUESTION 1  Day 1 (Alekhya)
from typing import List, Tuple 
def sort_by_tuple_sum(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
   return sorted(lst, key=lambda x: sum(x))

# Test Cases
print(sort_by_tuple_sum([(3, 1), (2, 2), (5, -1), (0, 0)]))  
print(sort_by_tuple_sum([(7, 3), (1, 2), (4, 5), (0, 1)]))  
print(sort_by_tuple_sum([(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]))  


# In[1]:


# Question 2 Day 1 (Alekhya)

from typing import List

def filter_strings(lst: List[str], k: int, m: int) -> List[str]:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    def count_vowels(s: str) -> int:
        return sum(1 for char in s if char.lower() in vowels)
    
    return [s for s in lst if len(s) >= k and count_vowels(s) >= m]

# Test Cases
print(filter_strings(["apple", "hi", "world", "yes", "python"], 4, 2))  
print(filter_strings(["education", "science", "art", "mathematics"], 5, 3))  


# In[3]:


#QUESTION 3 Day 2(Alekhya)
def length_of_last_word(s: str) -> int:
    return len(s.strip().split()[-1])

# Test Cases
print(length_of_last_word("Learn Python"))  
print(length_of_last_word(" coding is fun "))
print(length_of_last_word("   fly me   to   the moon  "))  


# In[1]:


#QUESTION 4 Day 2(Alekhya)
def search_range(nums, target):
    if target in nums:
        first = nums.index(target)
        last = len(nums) - 1 - nums[::-1].index(target) 
        return [first, last]
    return [-1, -1]

# Test Cases
print(search_range([5,7,7,8,8,10], 8))  
print(search_range([5,7,7,8,8,10], 6))  
print(search_range([], 0))  


# In[4]:


#Question 5: Product of Array Except Self.#Day 3(Alekhya)
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result
print(product_except_self([1, 2, 3, 4]))  
print(product_except_self([-1, 1, 0, -3, 3])) 


# In[5]:


#Question 6: Longest Substring Without Repeating Characters.#Day 3(Alekhya)
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length
print(length_of_longest_substring("abcabcbb"))  
print(length_of_longest_substring("bbbbb"))    
print(length_of_longest_substring("pwwkew")) 


# In[2]:


#Question 7: Minimum Difference Between Highest and Lowest of K Scores(Alekhya)--Day 4
def minimumDifference(nums, k):
    if k == 1:
        return 0  
    nums.sort() 
    min_diff = float('inf')
    for i in range(len(nums) - k + 1):
        min_diff = min(min_diff, nums[i + k - 1] - nums[i])
        return min_diff
print(minimumDifference([90], 1))
print(minimumDifference([9, 4, 1, 7], 2)) 


# In[3]:


#Question 8: Minimum Size Subarray Sum(Alekhya)--Day 4
def minSubArrayLen(target, nums):
    left = 0
    total = 0
    min_length = float('inf')
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_length = min(min_length, right - left + 1)
            total -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0
print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))  
print(minSubArrayLen(4, [1, 4, 4]))  
print(minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  


# In[6]:


#Question 9: Find Peak Element(Alekhya)--day 5
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:  
            right = mid
        else: 
            left = mid + 1

    return left  
print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))


# In[7]:


#Question 10: Largest Number(Alekhya)---day 5
from functools import cmp_to_key
def largestNumber(nums):
    def compare(x, y):
        return -1 if x + y > y + x else 1
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(compare))  
    result = ''.join(nums)
    return '0' if result[0] == '0' else result  
print(largestNumber([10, 2])) 
print(largestNumber([3, 30, 34, 5, 9]))  


# In[1]:


#Question 11: Longest Substring with At Most Two Distinct Characters(Alekhya)---day 6
from collections import defaultdict
def length_of_longest_substring_two_distinct(s: str) -> int:
    left = 0
    char_count = defaultdict(int)
    max_length = 0   
    for right in range(len(s)):
        char_count[s[right]] += 1      
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1          
        max_length = max(max_length, right - left + 1)    
    return max_length
print(length_of_longest_substring_two_distinct("eceba"))  
print(length_of_longest_substring_two_distinct("ccaabbb"))  


# In[4]:


#Question 12: Longest Palindromic Subsequence(Alekhya)--day 6
def longest_palindromic_subsequence(s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]    
    for i in range(n):
        dp[i][i] = 1   
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])  
    return dp[0][n-1]
print(longest_palindromic_subsequence("bbbab")) 
print(longest_palindromic_subsequence("cbbd"))   


# In[3]:


#Question 13: Valid Triangle Number(Alekhya)---day 7
def triangle_number(nums) -> int:
    nums.sort()
    count = 0
    n = len(nums)    
    for i in range(n-1, 1, -1):
        left, right = 0, i - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                count += (right - left)
                right -= 1
            else:
                left += 1
    return count
print(triangle_number([2, 2, 2, 4]))  
print(triangle_number([4, 2, 3, 4]))  


# In[5]:


#Question 14: Maximum Gap(Alekhya)---day 7
def maximum_gap(nums) -> int:
    if len(nums) < 2:
        return 0    
    nums.sort()
    max_gap = 0    
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i-1])    
    return max_gap
print(maximum_gap([3, 6, 9, 1]))  
print(maximum_gap([10]))         


# In[ ]:




