# no need to loop nums2 from the beginning for every i
# nums1, nums2 are both decreasing
# so for i we found the max j and for i+1, we can start from j
def maxDistance(nums1, nums2):
    maximum = 0
    j = -1
    for i, num in enumerate(nums1):
        while j+1 < len(nums2) and nums2[j+1] >= num:
            j += 1
            #print(f"{i} / {j}")
        maximum = max(maximum, j - i)
    return maximum

print(maxDistance([55,30,5,4,2], [100,20,10,10,5]))