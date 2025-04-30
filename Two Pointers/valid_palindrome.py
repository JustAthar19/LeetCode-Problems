# using two pointers
'''
input : 
s = "A man, a plan, a canal: Panama"
output = True
explanation = "amanaplanacanalpanama" is palindrom
'''

# Using Two Pointers
def is_palindrome_two_pointers(s):
    l, r = 0, len(s)-1
    while(l <= r):
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

def is_palindrome_compare_strings(s):
    new_str = ""
    for c in s:
        if c.isalnum():
            new_str += c.lower()
    return new_str == new_str[::-1]

print(is_palindrome_two_pointers("A man, a plan, a canal: Panama"))
print(is_palindrome_compare_strings("A man, a plan, a canal: Panama"))