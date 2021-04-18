# sort and unify the list
# find the index of 1
# if not found return 1
# since the list is unify and sorted, the list[index] should be index + 1 (i.e. a[0] = 1)

def firstMissingPositive(nums):
    nums = sorted(list(set(nums)))
    try:
        index = nums.index(1)
        nums = nums[index:]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
    except ValueError:
        return 1

print(firstMissingPositive([1,1000]))