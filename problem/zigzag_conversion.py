def convert(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    result = [""] * numRows
    index = 0
    step = -1
    for i in range(len(s)):
        print(index)
        result[index] += s[i]
        if i % (numRows - 1) == 0:
            step = - step
        index += step
    return ''.join(result)

print(convert("PAYPALISHIRING", 3))