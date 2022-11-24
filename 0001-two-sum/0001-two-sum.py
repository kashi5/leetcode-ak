class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_:
                return[i,hash_[complement]]
            hash_[nums[i]]=i