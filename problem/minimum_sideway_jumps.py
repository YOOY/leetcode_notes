# set the obstacle to inf which means the frog can be here
# for each lane, get the minimum step
def minSideJumps_dp(obstacles):
    path = [1,0,1]
    for o in obstacles:
        if o > 0:
            path[o-1] = float('inf')
        for i in range(3):
            if (i+1) != o:
                path[i] = min(path[i], path[(i+1) % 3] + 1, path[(i+2) % 3] + 1)
    return min(path)

print(minSideJumps_dp([0,1,2,3,0]))


# use set to keep track the possible lane we can go
# remove lane if obstacle in on next lane
def minSideJumps_set(obstacles):
    lane = set([2])
    count = 0
    for i in range(len(obstacles)-1):
        if obstacles[i+1] in lane:
            lane.remove(obstacles[i+1])
            # if there is no lane, whcih means we need to cross lane
            # calculate the possible lane we can jump to
            if not lane:
                lane = set([1,2,3]) ^ set([obstacles[i], obstacles[i+1]]) & set([1,2,3])
                count += 1
    return count
print(minSideJumps_dp([0,1,2,3,0]))