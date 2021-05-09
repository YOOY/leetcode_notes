def reinitializePermutation(n):
    count = 0
    ori_index = running_index = 1
    while True:
        if running_index % 2 == 1:
            running_index = (n/2 + (running_index-1)/2)
        else:
            running_index /= 2
        count += 1
        if running_index == ori_index:
            break
    return count

print(reinitializePermutation(10))