"""
Problem: Is Palindrome
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Category: Array & Hashing 
"""

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in nums:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest
