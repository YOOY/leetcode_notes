# calculate the sum and collect each diff
# for each diff try to find the number in nums1 which is closest to nums2[i]
# calculate the sum again to see if it was minimum

import bisect
def minAbsoluteSumDiff(nums1, nums2):
    sums = 0
    length = len(nums1)
    diffs = []
    length = len(nums1)
    for i in range(length):
        tmp = abs((nums1[i] - nums2[i]))
        sums += tmp
        diffs.append(tmp)
    minimum = float('inf')
    nums1 = sorted(nums1)
    for num, diff in zip(nums2, diffs):
        index = bisect.bisect_left(nums1, num)
        if index > 0:
            minimum = min(minimum, sums - diff + abs(nums1[index-1] - num))
        if index < length:
            minimum = min(minimum, sums - diff + abs(nums1[index] - num))
        #print(f"{num} / {diff} / {index} / {minimum}")
    return minimum % (10 ** 9 + 7)

print(minAbsoluteSumDiff([1,10,4,4,2,7], [9,3,5,1,7,4]))
        