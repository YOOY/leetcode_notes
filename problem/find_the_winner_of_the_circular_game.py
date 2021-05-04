def findTheWinner(n, k):
    candidate = [i for i in range(1, n+1)]
    while n > 1:
        next_head = (k % n)
        if next_head > 0:
            candidate = candidate[next_head:] + candidate[0:next_head-1]
        else:
            candidate = candidate[0:-1]
        n -= 1
    return candidate[0]

print(findTheWinner(5, 2))