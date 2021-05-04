from collections import defaultdict
def countNicePairs(nums):
    result = defaultdict(int)
    ans = 0
    for i in nums:
        tmp = i - rev(i)
        result[tmp] += 1
    
    for i in result.values():
        ans += i * (i-1) // 2
    return ans % (10**9 + 7)

def rev(num):
    return int(str(num)[::-1])

print(countNicePairs([13,10,35,24,76]))