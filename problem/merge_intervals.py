def merge(intervals):
    intervals = sorted(intervals)
    result = []
    for i in intervals:
        if not result or i[0] > result[-1][1]:
            result.append(i)
        else:
            result[-1] = [min(result[-1][0], i[0]), max(result[-1][1], i[1])]
    return result

print(merge([[1,4],[0,0],[2,5]]))