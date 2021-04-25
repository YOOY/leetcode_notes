def search_two_pointer(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        if target == nums[l]:
            return l
        if target == nums[r]:
            return r
        l += 1
        r -= 1
    return -1

print(search_two_pointer([4,5,6,7,0,1,2], 7))