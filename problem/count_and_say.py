def countAndSay(n):
    if n == 1:
        return '1'
    string = countAndSay(n-1)
    result = ""
    tmp = ""
    for c in string:
        if not tmp or tmp[0] == c:
            tmp += c
        elif tmp[0] != c:
            result += f"{len(tmp)}{tmp[0]}"
            tmp = c
    result += f"{len(tmp)}{tmp[0]}"
    print(f"string is {string} / n = {n} / result = {result}")
    return result

print(countAndSay(3))