def maxSlidingWindow(nums, k):
    result = []
    queue = deque()
    for index, num in enumerate(nums):
        while queue and nums[queue[-1]] <= num:
            queue.pop()
        queue.append(index)
        if queue[0] + k == index:
            queue.popleft()
        if index + 1 >= k:
            result.append(nums[queue[0]])
    return result

print(maxSlidingWindow([1,3,1,2,0,5], 3))