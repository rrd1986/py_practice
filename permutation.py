def Permutation(word):
    if len(word) == 1:
        return word
    final = []
    for i in range(len(word)):
        pre = word[:i]
        cur = word[i]
        post = word[i+1:]
        for p in Permutation( pre + post):
            final.append(cur + p)
    return final


print(len(Permutation("ABCD")))



