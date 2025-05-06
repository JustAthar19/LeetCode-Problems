

nums = [1,1,2,3,3,4]


def remove_duplicates(nums):
    j = 1
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
            
    return nums

print(remove_duplicates(nums))