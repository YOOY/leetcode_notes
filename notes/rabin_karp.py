# rolling hash
from collections import defaultdict

def rabin_karp(s, p):
    mod = 101
    base = 26
    hash_p = rolling_hash = 0
    result = defaultdict(int)
    length_s = len(s)
    length_p = len(p)
    for i in range(length_p):
        hash_p = (hash_p * base + ord(p[i])) % mod
        rolling_hash = (rolling_hash * base + ord(s[i])) % mod
    for i in range(length_s - length_p):
        rolling_hash -= (ord(s[i]) * (base**(length_p-1))) % mod
        rolling_hash = (rolling_hash * base + ord(s[i+length_p])) % mod
        if rolling_hash == hash_p:
            result[s[i+1:i+length_p+1]] += 1
    print(result)



print(rabin_karp('thisisaballandthatisapen', 'apen'))