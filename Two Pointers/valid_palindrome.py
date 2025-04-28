# using two pointers
'''
input : 
s = "A man, a plan, a canal: Panama"
output = True
explanation = "amanaplanacanalpanama" is palindrom
'''

def is_palindrome(s):
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

print(is_palindrome("A man, a plan, a canal: Panama"))