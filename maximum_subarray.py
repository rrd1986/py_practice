# Largest Sum Contiguous Subarray

# [-2, -3, 4, -1, -2, 1, 5, -3]  -> ans 7

from typing import List

def max_subarray_sum(nums: List[int]) -> int:
    cur_sum = 0
    max_sum = nums[0]
    
    for i in nums:
        cur_sum = cur_sum + i
        if cur_sum < 0:
            cur_sum = 0
        max_sum = max(max_sum, cur_sum)
    return max_sum

if __name__ == "__main__":
    nums = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(max_subarray_sum(nums))
 

