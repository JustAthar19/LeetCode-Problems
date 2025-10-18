"""
Problem: Remove Duplicates - Input Array is Sorted
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Category: Two pointers
"""


nums = [1,1,2,3,3,4]


def remove_duplicates(nums):
    j = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i] # overwrite
            j += 1
            
    return nums

print(remove_duplicates(nums))