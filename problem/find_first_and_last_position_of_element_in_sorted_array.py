def searchRange(nums, target):
    l = 0
    r = len(nums) - 1
    first = last = None
    while (l <= r) and (not first or not last):
        if nums[l] == target and not first:
            first = l
        if nums[r] == target and not last:
            last = r
        if not first:
            l += 1
        if not last:
            r -= 1
    return [first, last]

print(searchRange([5,7,7,8,8,8,10], 8))
