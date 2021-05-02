# max number is 2 ** maximumBit -1
# X ^ k = max_number
# k = X ^ max_number

def getMaximumXor(nums, maximumBit):
    result = []
    xor = 0
    maximum = (1 << maximumBit) -1
    for i in nums:
        xor ^= i
        result.append(maximum ^ xor)
    return result[::-1]

print(getMaximumXor([0,1,1,3], 2))