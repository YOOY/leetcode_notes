from collections import Counter
def countNicePairs(nums):
    result = Counter()
    ans = 0
    for i in nums:
        tmp = i - rev(i)
        ans += result[tmp]
        result[tmp] += 1
    return ans % (10**9 + 7)

def rev(num):
    return int(str(num)[::-1])