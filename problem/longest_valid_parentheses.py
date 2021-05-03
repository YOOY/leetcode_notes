# initialize a list of 0
# for each '(' found, put the index into stack
# for each valid () found, mark their value to 1 in the list of 0
# count 1's

def longestValidParentheses(s):
    stack = []
    a = ['0'] * len(s)
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if not stack:
                continue
            else:
                index = stack.pop()
                a[i] = '1'
                a[index] = '1'
    print(a)
    longest = max(''.join(a).split('0')).count('1')
    return longest

print(longestValidParentheses("()(()"))