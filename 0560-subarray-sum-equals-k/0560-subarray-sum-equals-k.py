class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash map solution
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
        
#         using prefixsum time O(n2) TLE for python
#         count = 0
#         prefix_sum_list =[0]
#         prefix_sum = 0
#         for i in nums:
#             prefix_sum += i
#             prefix_sum_list.append(prefix_sum)
#         print(prefix_sum_list)
#         for x in range(len(nums)):
#             num_1 = prefix_sum_list[x]
#             for y in range(x+1,len(nums)+1):
#                 num_2 = prefix_sum_list[y]
#                 if k == num_2 - num_1:
#                     count += 1
#         return count
            
            
            
                
        