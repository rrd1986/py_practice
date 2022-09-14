
def FindScore(braces: str):
    stack = []
    final_score = 0
    for b in braces:
        if b  == "(":
            score = 1
            stack.append(b)
        else:
            if len(stack):
                stack.pop()
                if len(stack) == 0:
                    score =score * 1
                    final_score = final_score + score
                else:    
                    score =score * 2
    if len(stack):
        print("unbalanced")
    else:
        print(final_score)
        print("balanced")



if __name__ == "__main__":
    FindScore("))))")

