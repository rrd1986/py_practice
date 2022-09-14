
# Given an array of integers nums and an integer target , return indices of the two numbers such that they add up to target 

from typing import List

# [6, 7, 11, 15, 3, 6, 5, 3]  -- > 6
#   6 - 6 = 0 {0:0}
#   6 - 7 = -1 { 0:0, -1: 1} 


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
            print("Hi")
            print(f"{target }")
            print(f"{num }")
            print(f"{target - num}, {i}")
            print(f"{seen[target - num ]}, {i}")
            return [seen[target - num ], i]
        else:
            seen[target - num ] = i
            print(seen)


if __name__ == "__main__":
    print(two_sum([6, 7, 11, 15, 3, 5, 3], 6))
