class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_till_now=nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            s = nums[i]
            max_sum = max(s,max_sum+s)
            max_sum_till_now = max(max_sum_till_now,max_sum)
        return max_sum_till_now
            