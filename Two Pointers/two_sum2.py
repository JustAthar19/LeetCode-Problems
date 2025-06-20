"""
Problem: Two Sum II - Input Array is Sorted
Link: https://leetcode.com/problems/two-sum/
Category: Two pointers
"""



numbers = [2,7,11,15]
target = 9

# brute force - time limit exceeded 
# def two_sum(numbers, target):
#     for i in range(len(numbers)-1):
#         for j in range(i+1, len(numbers)):
#             if (numbers[i] + numbers[j] == target):
#                 return [i + 1, j + 1]


# two pointers 
def two_sum(numbers, target):
    l, r = 0, len(numbers)-1
    while (l<=r):
        if numbers[l] + numbers[r] == target: 
            return[l + 1, r + 1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        elif numbers[l] + numbers[r] > target:
            r -= 1
    return []



print(two_sum(numbers, target))