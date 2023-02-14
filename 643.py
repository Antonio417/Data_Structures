# Leetcode Problem: 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10^-5 will be accepted.

import numpy as np

## Naive Solutions
def find_max_average(nums, k):
    temp_max = np.NINF
    for i in range(len(nums)):
        naive_sum = 0
        for j in range(0,k):
            if not(i+(k-1) > len(nums)-1):
                naive_sum += nums[i+j]
            else:
                i = len(nums)
                j = k
        if naive_sum != 0:
            print(np.floor(naive_sum/k).astype(int))
            temp_max = max(temp_max, (naive_sum/k))
    if temp_max== np.NINF:
        return 0
    return temp_max

k = 4
nums = [1,12,-5,-6,50,3]
answer = find_max_average(nums, k)
print(answer)

