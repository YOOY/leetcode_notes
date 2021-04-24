# run each character in s
# divide s[i:i+words_len] into group of word_len
# to see if both list are the same

def findSubstring(s, words):
    word_len = len(words[0])
    words_len = len(words) * word_len
    result = []
    s_len = len(s)
    compared = sorted(words)
    candidate = s[0:1-words_len] if words_len != 1 else s
    for i in range(len(candidate)):
        a = s[i:i+words_len]
        b = [a[x:x+word_len] for x in range(0, len(a),word_len)]
        b = sorted(b)
        if b == compared:
            result.append(i)
        
    return list(set(result))


a = findSubstring("a", ["a"])
print(a)
