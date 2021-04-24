# permutation of [1,2,3]
# [1,2,3] -> [1,3,2] -> [2,1,3] -> [2,3,1] -> [3,1,2] -> [3,2,1]
# for [1,3,2] the next permutaion is [2,1,3]
def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    clean = True
    index_a = index_b = 0
    for i in range(length-1, 0, -1):
        if nums[i] > nums[i-1]:
            clean = (i == 0)
            index_a = i - 1
            break
    if not clean:
        for i in range(length-1, 0, -1):
            if nums[index_a] < nums[i]:
                index_b = i
                break
        print(index_a, index_b)
        nums[index_a], nums[index_b] = nums[index_b], nums[index_a]
        nums[index_a+1:] = sorted(nums[index_a+1:])
    else:
        nums.reverse()
    print(nums)

nextPermutation([1,3,2])