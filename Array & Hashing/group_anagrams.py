"""
Problem: Is Palindrome
Link: https://leetcode.com/problems/group-anagrams
Category: Array
"""

def groupAnagrams(strs):
    anagram_dict = {}
    for s in strs:
        sorted_words = "".join(sorted(s))
        if sorted_words not in anagram_dict:
            anagram_dict[sorted_words] = []
        anagram_dict[sorted_words].append(s)
    return list(anagram_dict.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))