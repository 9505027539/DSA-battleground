#!/usr/bin/env python
# coding: utf-8

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


# In[2]:


# QUESTION 1  Day 1 (Alekhya)
from typing import List, Tuple 
def sort_by_tuple_sum(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
   return sorted(lst, key=lambda x: sum(x))

# Test Cases
print(sort_by_tuple_sum([(3, 1), (2, 2), (5, -1), (0, 0)]))  
print(sort_by_tuple_sum([(7, 3), (1, 2), (4, 5), (0, 1)]))  
print(sort_by_tuple_sum([(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]))  


# In[3]:


#QUESTION 3 Day 2(Alekhya)
def length_of_last_word(s: str) -> int:
    return len(s.strip().split()[-1])

# Test Cases
print(length_of_last_word("Learn Python"))  
print(length_of_last_word(" coding is fun "))
print(length_of_last_word("   fly me   to   the moon  "))  


# In[4]:


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

