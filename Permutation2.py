

def Permutation(word: str) -> str:
    if len(word) == 1:
        return [word]
    result = []
    for i in range(len(word)):
        pre = word[:i]
        current = word[i]
        post = word[i+1:]
        for p in Permutation(pre + post):
            result.append(current + p)

    return result

if __name__ == "__main__":
    print(Permutation("ABCDE"))
    print(len(Permutation("ABCDE")))
