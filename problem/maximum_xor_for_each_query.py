# XOR
# 0 ^ 0 = 0
# 0 ^ 1 = 1
# 1 ^ 0 = 1
# 1 ^ 1 = 0
# max number is 2 ** maximumBit -1
# xor ^ k = mx
# xor ^ xor ^ k = xor ^ mx
# 0 ^ k = xor ^ mx
# k = xor ^ mx

def getMaximumXor(nums, maximumBit):
    result = []
    xor = 0
    maximum = (1 << maximumBit) -1
    for i in nums:
        xor ^= i
        result.append(maximum ^ xor)
    return result[::-1]

print(getMaximumXor([0,1,1,3], 2))