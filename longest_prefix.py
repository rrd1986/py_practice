# input: ["rashmi", "ranjan", "ramji", "ras"]


from typing import List

def longest_prefix(l: List[str]) -> str:
    min_length = len(l[0])
    for s in l:
        if len(s) < min_length:
            min_length = len(s)
    if min_length == 0:
        return ""
    longest_prefix = []    
    index = 0
    while index < min_length:
        check = True
        for i in range(1, len(l)):
            if l[0][index] != l[i][index]:
                check = False
        if check:
            longest_prefix.append(l[i][index])
        else:
            return "".join(longest_prefix)
        index += 1
    return "".join(longest_prefix)


if __name__ == "__main__":
    l = ["rashmi", "ranjan", "ramji", "ras"]
    l2 = ["ranj", "ranjan", "ranjandib"]
    lp = longest_prefix(l2)
    print(lp)


