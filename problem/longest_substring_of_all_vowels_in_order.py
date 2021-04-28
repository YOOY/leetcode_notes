def longestBeautifulSubstring(word):
    target = 'aeiou'
    max_match = 0
    count = 0
    index = 0
    for i in word:
        #print(f"i {i} / count {count}/index {target[index]}")
        if i == target[index]:
            count += 1
        elif index < len(target) -1 and i == target[index+1] and count != 0:
            index += 1
            count += 1
        else:
            if index == len(target) - 1:
                max_match = max(count, max_match)
            index = 0
            count = 0
            if i == target[index]:
                count += 1
    if index == len(target) - 1:
        max_match = max(count, max_match)
    return max_match

print(longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))