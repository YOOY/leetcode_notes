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

print(permute([1,2,3]))
