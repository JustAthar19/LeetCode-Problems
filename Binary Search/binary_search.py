"""
Problem: Two Sum II - Input Array is Sorted
Link: https://leetcode.com/problems/binary-search/
Category: Binary Search
"""

nums = [-1,0,3,5,9,12]
target = 9

def binary_search(nums, target):
    l, r = 0, len(nums)-1
    while l<=r:
        mid = (l + r) // 2 
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
    return -1


print(binary_search(nums, target))