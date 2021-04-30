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
    #print(zero_index)
    for index in range(zero_length):
        if index == 0:
            max_length = max(max_length, zero_index[index+1] - 1)
        elif index == zero_length - 1:
            max_length = max(max_length, nums_length - zero_index[index-1] - 2)
        else:
            max_length = max(max_length, zero_index[index+1] - zero_index[index-1] - 2)
        #print(f"{zero_index[index]} / {max_length}")
    return max_length

print(longestSubarray([0,1,1,1,0,1,1,0,1]))