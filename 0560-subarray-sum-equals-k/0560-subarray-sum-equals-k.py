class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        count = 0
        dict_ = {0:1}
        for i in nums:
            sum_ += i
            target = sum_ - k 
            if target in dict_:
                count+=dict_.get(target, 0)
            dict_[sum_]=dict_.get(sum_, 0) +1
        return count
            
                
        