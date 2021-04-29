# for a 3 * 7 matrix
# the first row are always 1 way
# the a[1][0] still 1
# the a[1][1] is a[0][1] + a[1][0]

def uniquePaths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for i in range(1, n):
            dp[i] = dp[i-1] + dp[i]
    return dp[-1]

print(uniquePaths(3,7))