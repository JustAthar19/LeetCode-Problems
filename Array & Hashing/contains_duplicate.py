"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Category: Array
"""

def contains_duplicate(nums):
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == nums[i+1] : return True
    return False


nums = [21, 22, 19, 81, 18, 22]

print(contains_duplicate(nums))