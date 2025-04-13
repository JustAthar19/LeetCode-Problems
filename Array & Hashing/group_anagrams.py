"""
Problem: Is Palindrom
Link: https://leetcode.com/problems/group-anagrams
Category: Array
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            sorted_words = ''.join(sorted(s))
            if sorted_words not in anagram_dict:
                anagram_dict[sorted_words] = []
            anagram_dict[sorted_words].append(s)
        return list(anagram_dict.values)