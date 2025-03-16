#!/usr/bin/env python
# coding: utf-8

# In[1]:


# QUESTION 1  Day 1 (Alekhya)
from typing import List, Tuple 
def sort_by_tuple_sum(lst: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
   return sorted(lst, key=lambda x: sum(x))

# Test Cases
print(sort_by_tuple_sum([(3, 1), (2, 2), (5, -1), (0, 0)]))  
print(sort_by_tuple_sum([(7, 3), (1, 2), (4, 5), (0, 1)]))  
print(sort_by_tuple_sum([(8, -3), (1, 1), (2, 0), (5, 5), (3, 2)]))  


# In[2]:


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

