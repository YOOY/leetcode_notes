# three scenario
# s1 at the front
# s1 at the end
# some s1 at the front and some at the end
# check from head and tail to see if s1 is fit

def areSentencesSimilar(sentence1, sentence2):
    if len(sentence1) > len(sentence2):
        sentence1, sentence2 = sentence2, sentence1
    words1, words2 = sentence1.split(' '), sentence2.split(' ')
    l = 0
    r = -1
    
    while words1 and words1[0] == words2[l]:
        words1.pop(0)
        l += 1
    while words1 and words1[-1] == words2[r]:
        words1.pop()
        r -= 1
        
    return not words1

print(areSentencesSimilar("A A Aa", "A Aa"))