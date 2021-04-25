def groupAnagrams(strs):
    result = {}
    for string in strs:
        key = tuple(sorted(string))
        tmp = result.get(key, [])
        tmp.append(string)
        result[key] = tmp
    return list(result.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))