def threeSumClosest(nums, target):
    length = len(nums)
    minimum = None
    result = None
    nums = sorted(nums)
    for l in range(length - 2):
        if l > 0 and nums[l] == nums [l-1]:
            continue
        m = l + 1
        r = length - 1
        remain = target - nums[l]
        while m < r:
            sums = nums[m] + nums[r]
            total = nums[l] + sums
            diff = abs(target - total)
            if not minimum or minimum > diff:
                minimum = diff
                result = total
            if sums > remain:
                r -= 1
                while r > m and nums[r] == nums[r+1]:
                    r -= 1
            elif sums < remain:
                m += 1
                while m < r and nums[m] == nums[m-1]:
                    m += 1
            else:
                return result
    return result

print(threeSumClosest([-1,2,1,4], -1))