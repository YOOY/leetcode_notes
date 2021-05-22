def minOperations(boxes):
    result = [0] * len(boxes)
    for index, ball in enumerate(boxes):
        if ball == '1':
            for i in range(len(boxes)):
                result[i] += abs(index-i)
    return result

print(minOperations("001011"))

# for each i, the total move is total moves of left (0 to (i-1)) and right ((i+1) to (n))
def minOperations_v2(boxes):
    left_move = left_cost = right_move = right_cost = 0
    length = len(boxes)
    result = [0] * length
    for i in range(1, length):
        if boxes[i-1] == '1':
            left_cost += 1
        left_move += left_cost
        result[i] += left_move
    for i in range(length-2, -1, -1):
        if boxes[i+1] == '1':
            right_cost += 1
        right_move += right_cost
        result[i] += right_move
    return result

print(minOperations_v2("001011"))