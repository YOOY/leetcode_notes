def getMinSwaps(num, k):
    nums1 = num
    num = list(num)
    nums1 = list(nums1)
    nums1 = get_k_permutation(nums1, k)
    return get_count(nums1, num)            
    
def get_k_permutation(nums, k):
    length = len(nums)

    while k > 0:
        index_a = index_b = None
        for i in range(length-1, 0, -1):
            if nums[i] > nums[i-1]:
                index_a = i - 1
                break
        if index_a is None:
            break
        k -= 1
        for i in range(length-1, 0, -1):
            if nums[i] > nums[index_a]:
                index_b = i
                break
        nums[index_a], nums[index_b] = nums[index_b], nums[index_a]
        nums[index_a+1:] = sorted(nums[index_a+1:])

    return nums

def get_count(nums, nums1):
    count = 0
    nums = list(nums)
    nums1 = list(nums1)
    for i in range(len(nums)):
        if nums[i] != nums1[i]:
            j = i
            while nums[j] != nums1[i]:
                j += 1
            count += j - i
            tmp = nums.pop(j)
            nums.insert(i, tmp)
    return count

print(getMinSwaps("5489355142", 4))