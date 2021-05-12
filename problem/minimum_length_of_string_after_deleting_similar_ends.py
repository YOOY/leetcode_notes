def minimumLength(s):
    l = 0
    r = len(s) - 1
    while l < r:
        #print(f"before {l},{r}")
        if s[l] != s[r] :
            break
        # to prevent l bigger than r
        while s[l] == s[l+1] and l < r-1:
            l += 1
        while s[r] == s[r-1] and l < r-1:
            r -= 1
        #print(f"after {l},{r}")
        l += 1
        r -= 1
    return r-l+1

print(minimumLength('cabaabac'))