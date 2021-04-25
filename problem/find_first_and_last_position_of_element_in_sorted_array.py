def searchRange(nums, target):
    l = 0
    r = len(nums) - 1
    first = last = -1
    while (l <= r) and (first == -1 or last == -1):
        if nums[l] == target and first == -1:
            first = l
        if nums[r] == target and last == -1:
            last = r
        if first == -1:
            l += 1
        if last == -1:
            r -= 1
    return [first, last]

print(searchRange([5,7,7,8,8,10], 8))
