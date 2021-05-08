import heapq
def maxAverageRatio(classes, extraStudents):
    heap = [(a/b - (a+1)/(b+1), a, b) for a, b in classes]
    heapq.heapify(heap)

    while extraStudents > 0:
        _, class_pass, class_students = heapq.heappop(heap)
        class_pass += 1
        class_students += 1
        heapq.heappush(heap, (class_pass/class_students - (class_pass+1)/(class_students+1), class_pass, class_students))
        extraStudents -= 1
    return sum([a/b for _,a,b in heap]) / len(classes)

print(maxAverageRatio([[1,2],[3,5],[2,2]], 2))