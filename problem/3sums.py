def threeSum(nums):
    result = []
    length = len(nums)
    if length < 3:
        return result
    nums = sorted(nums)
    print(nums)
    for l in range(length-2):
        print(l)
        if l > 0 and nums[l] == nums[l-1]:
            continue
        if nums[l] > 0:
            break
        m = l + 1
        r = length - 1
        while m < r:
            sums  = nums[l] + nums[m] + nums[r]
            if sums > 0:
                r -= 1
            elif sums < 0:
                m += 1
            else:
                result.append([nums[l], nums[m], nums[r]])
                m += 1
                r -= 1
                while m < r and nums[m] == nums[m-1]:
                    m += 1
                while r > m and nums[r] == nums[r+1]:
                    r -= 1
    return result

print(threeSum([1,3,5,7,0,-1,-3,-7]))
