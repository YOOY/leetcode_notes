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


def maxIceCream_v2(costs, coins):
    sums = 0
    costs = sorted(costs)
    for index in range(len(costs)):
        if sums + costs[i] <= coins:
            sums += costs[i]
        elif sums + costs[i] > coins:
            return i + 1

print(maxIceCream([1,3,2,4,1], 7))