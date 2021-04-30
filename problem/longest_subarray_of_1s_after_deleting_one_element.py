# get all 0's index into zero_index
# calculate 1 by zero_index[index-1] to zero[index+1] - 2
# handle case for first/last index

def longestSubarray(nums):
    zero_index = []
    nums_length = len(nums)
    max_length = 0
    for i in range(nums_length):
        if nums[i] == 0:
            zero_index.append(i)
    zero_length = len(zero_index)
    if not zero_index or zero_length == 1:
        return nums_length - 1
    if zero_length == nums_length:
        return max_length
    for index in range(zero_length):
        if index == 0:
            max_length = max(max_length, zero_index[index+1] - 1)
        elif index == zero_length - 1:
            max_length = max(max_length, nums_length - zero_index[index-1] - 2)
        else:
            max_length = max(max_length, zero_index[index+1] - zero_index[index-1] - 2)
    return max_length


# count 1 until meet 0 and add count to array
# reset count and redo step 1
# sum array[i] + array[i+1] to get max length
def longestSubarray_v2(nums):
    ones = []
    count = 0
    for i in nums:
        if i == 1:
            count += 1
        else:
            ones.append(count)
            count = 0
    ones.append(count)
    if len(ones) == 1:
        return ones[0] - 1
    max_length = ones[0]
    for i in range(len(ones)-1):
        max_length = max(max_length, ones[i] + ones[i+1])

    return max_length


print(longestSubarray([0,1,1,1,0,1,1,0,1]))
print(longestSubarray_v2([0,1,1,1,0,1,1,0,1]))
