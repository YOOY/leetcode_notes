def permuteUnique(nums):
    result = []
    dfs(nums, [], result)
    return result

def dfs(nums, path, result):
    if not nums:
        result.append(path)
    for i in range(len(nums)):
        if i > 0 and nums[i] in nums[:i]:
            continue
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], result)

print(permuteUnique([3,3,0,3]))