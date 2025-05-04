"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Category: Array
"""

def twoSum(nums, target):
    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap: 
            return prevMap[diff], i
    prevMap[n] = i

