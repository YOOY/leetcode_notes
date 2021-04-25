from copy import deepcopy
def permute(nums):
    limit = len(nums)
    result = []
    backtracking(nums, [], limit, result)
    return result
    

def backtracking(nums, container, limit, result):
    if len(container) == limit:
        result.append(deepcopy(container))
        return container
    for i in nums:
        if i not in container:
            container.append(i)
            backtracking(nums, container, limit, result)
            container.remove(i)

def permute_dfs(nums):
    res = []
    dfs(nums, [], res)
    return res
    
def dfs(nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in range(len(nums)):
        print(f"i is {i} / nums is {nums} / path = {path}")
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

print(permute([1,2,3]))
print(permute_dfs([1,2,3]))
