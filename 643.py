# Leetcode Problem: 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10^-5 will be accepted.

## Naive Solutions
def find_max_average(nums, k):
    temp_max = float('-inf')
    for i in range(len(nums)):
        naive_sum = 0
        for j in range(0,k):
            if not(i+(k-1) > len(nums)-1):
                naive_sum += nums[i+j]
            else:
                i = len(nums)
                j = k
        if naive_sum != 0:
            temp_max = max(temp_max, (naive_sum/k))
    if temp_max== float('-inf'):
        return 0
    return temp_max

## Sliding Window Solutions
def find_max_average_sliding_window(nums,k):
    window_sum = 0
    start = 0
    temp_max = float('-inf')
    for end in range(len(nums)):
        window_sum += nums[end]
        if (end - start + 1) == k:
            # Calculate Average
            temp_max = max(temp_max, (window_sum/k))
            window_sum -= nums[start]
            start += 1
    return temp_max

k = 4
nums = [1,12,-5,-6,50,3]
naive_answer = find_max_average(nums, k)
sliding_window_answer = find_max_average_sliding_window(nums, k)
print("naive answer: ", naive_answer)
print("sliding window answer: ", sliding_window_answer)

