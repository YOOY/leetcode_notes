# push procdess time and index for those enqueue time is qualify

import heapq
def getOrder(tasks):
    result = []
    tasks = sorted([(etime, ptime, index) for index, (etime, ptime) in enumerate(tasks)])
    cpu_time = i = 0
    heap = []
    while len(result) < len(tasks):
        while i < len(tasks) and tasks[i][0] <= cpu_time:
            heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
            i += 1
        if heap:
            ptime, index = heapq.heappop(heap)
            result.append(index)
            cpu_time += ptime
        else:
            cpu_time = tasks[i][0]
    return result

print(getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))