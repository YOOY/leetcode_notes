def maxValue(n, index, maxSum):
    maxSum -= n
    ans = 1
    i = 0
    cost = 0
    while maxSum > 0:
        if cost < n:
            left_index = max(index - i, 0)
            right_index = min(index + i, n-1)
            cost = right_index - left_index + 1
        if cost == n:
            a, maxSum = divmod(maxSum, n)
            ans += a
        elif maxSum - cost >= 0:
            ans += 1
        i += 1
        maxSum -= cost
    return ans

print(maxValue(6, 1, 10))