# sliding window
# key is sum of nums[l:index] + k must bigger than nums[index] * number of element from l to index

def maxFrequency(nums, k):
    nums = sorted(nums)
    max_frequency = 1
    l = 0
    sums = 0
    for index, num in enumerate(nums):
        sums += num
        while l < index and sums + k < num * (index - l + 1):
            sums -= nums[l]
            l += 1
        max_frequency = max(max_frequency, index - l + 1)
    return max_frequency

print(maxFrequency([3,9,6], 2))