nums = [1,1,1,2,2,3]
k  = 2

count = {}
freq = [[] for i in range(len(nums) + 1)]
# Populate the dictionary
for n in nums:
    count[n] = 1 + count.get(n, 0)
# iterate through count dict and populate the freq list

print(f"{count}\n")

for c,n in count.items():
    freq[c].append(n)

print(f"{freq}\n")
res = []
for i in range(len(nums) - 1, 0, -1):
    for n in freq[i]:
        res.append(n)
    if len(res) == k : print("got em")
    else: print("Not Found")
print(f"{res}\n")

