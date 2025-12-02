"""
Problem: Longest Repeating Character Replacement
Link: https://leetcode.com/problems/longest-repeating-character-replacement/
Category: Sliding Window
"""
s = "ABAB"
k = 2

def characterReplacement(s, k):
    l = 0
    res = 0
    count = {}
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r],0)
        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, (r - l + 1))
    return res

print(characterReplacement(s,k))