def selection_sort(nums):
    result = []
    minimum = nums[0]
    length = len(nums)
    for _ in range(length-1):
        for i in nums:
            if i < minimum:
                minimum = i
        result.append(minimum)
        nums.remove(minimum)
        minimum = nums[0]
    result.append(nums[0])
    return result

def insertion_sort(nums):
    for i in range(1, len(nums)):
        index = i
        while index > 0 and (nums[index] < nums[index-1]):
            nums[index], nums[index-1] = nums[index-1], nums[index]
            index -= 1
    return nums

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums.pop()
    left = [i for i in nums if i < pivot]
    right = [i for i in nums if i >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(nums):
    length = len(nums)
    if length == 1:
        return nums

    # divide
    index = length >> 1
    left = merge_sort(nums[:index])
    right = merge_sort(nums[index:])

    # merge left / right
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result


print(selection_sort([9,1,23,0,100]))
print(insertion_sort([9,1,23,0,100]))
print(quick_sort([9,1,23,0,100]))
print(merge_sort([5, 3, 8, 6, 4, 2, 7, 1, 4]))