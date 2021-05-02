import heapq
def maxIceCream(costs, coins):
    heapq.heapify(costs)
    count = 0
    while costs:
        cost = heapq.heappop(costs)
        if coins >= cost:
            coins -= cost
            count += 1
        else:
            break
    return count

print(maxIceCream([1,3,2,4,1], 7))