nums = [1,1,1,2,2,3]
k  = 2

def topKfrequentElement(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+ 1)]
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    # count = { 1:3 , 2:2 , 3:1 } 
    for n, c in count.items():
        freq[c].append(n)
    # freq = [[], [3], [2], [1], [], [], []]
    res = []
    for i in range(len(freq) - 1, 0, -1): # looping from the last index of the array becuse we want the most frequent element
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    return []

print(topKfrequentElement(nums,k))