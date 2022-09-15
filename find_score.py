
# (((())))  1 * 2 * 2 * 2 = 8
# ()) invalid
# ((()))(()) 1 * 2 * 2 + 1 * 2 = 6
# ))))(((( -1


def findScore(braces: str) -> int:
    stack = []
    counter = 0
    score = 0
    for i in braces:
        if i == "(":
            stack.append(i)
            counter += 1
        elif i == ")":
            try:
                stack.pop()
            except:
                return -1
        if len(stack) == 0:
            score = score + 2**(counter -1)
            counter = 0
    if len(stack) != 0:
        return -1                
    else:
        return score


if __name__ == "__main__":
    print(findScore("(((())))"))

    print(findScore("())"))

    print(findScore("((()))(())"))

    print(findScore("))))(((("))


