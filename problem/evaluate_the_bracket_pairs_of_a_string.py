from collections import defaultdict
def default_value():
    return '?'
def evaluate(s, knowledge):
    key = ""
    result = ""
    keyword = False
    knowledges = defaultdict(default_value)
    for i in knowledge:
        knowledges[i[0]] = i[1]
    
    for i in s:
        if i == '(':
            keyword = True
        elif i == ')':
            keyword = False
            result += knowledges[key]
            key = ""
        elif keyword:
            key += i
        else:
            result += i
    return result

print(evaluate("(name)is(age)year(so)ld", [["name","bob"],["age","two"]]))