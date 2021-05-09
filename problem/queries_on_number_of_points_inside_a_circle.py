# a**2 + b**2 <= r**2

def countPoints(points, queries):
    result = [0] * len(queries)
    for i in range(len(queries)):
        x = queries[i][0]
        y = queries[i][1]
        r = queries[i][2] ** 2
        for point in points:
            if (point[0] - x) ** 2 + (point[1] - y) ** 2 <= r:
                result[i] += 1
    return result

print(countPoints([[1,3],[3,3],[5,3],[2,2]], [[2,3,1],[4,3,1],[1,1,2]]))