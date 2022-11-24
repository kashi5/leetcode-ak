class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_list = {}
        for i in nums:
            if i in dict_list:
                return True
            dict_list[i]=True
        return False