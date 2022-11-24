class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1,len(nums)):
            s =nums[i]
            temp_max = max(s,s*max_so_far,s*min_so_far)
            min_so_far = min(s,s*max_so_far,s*min_so_far)
            
            max_so_far =temp_max 
            result= max(max_so_far,result)
        return result