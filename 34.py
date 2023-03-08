class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.start_idx(nums, target)
        end = self.end_idx(nums, target)

        return start, end
    
    def start_idx(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left+right)//2
            if target == nums[middle]:
                if(middle == 0 or nums[middle-1] != target and middle-1>=0):
                    return middle
                else:
                    right = middle - 1
            elif target >= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    
    def end_idx(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left+right)//2
            if target == nums[middle]:
                if (middle == len(nums)-1 or nums[middle+1] != target and middle+1 <len(nums)):
                    return middle
                else:
                    left = middle + 1
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle -1
        return -1
