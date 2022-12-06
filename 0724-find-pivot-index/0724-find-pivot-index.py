class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S= sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            m = S -leftsum - x
            if leftsum == (S -leftsum - x):
                return i
            leftsum += x
        return -1