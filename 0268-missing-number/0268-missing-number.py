class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     for i in range(len(nums)):
    #         if i not in nums:
    #             return i
    #     return len(nums)
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        total_sum = size * (size+1) //2
        num_sums = 0
        for i in nums:
            num_sums += i
        return total_sum -num_sums
            
        