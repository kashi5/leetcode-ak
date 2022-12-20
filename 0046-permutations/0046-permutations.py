class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]
        self.permuteHelper(0,nums,result)
        return result

    def permuteHelper(self,i,nums,result):
        if i ==len(nums) -1:
            result.append(nums[:])
        else:
            for j in range(i,len(nums)):
                self.swap(nums,i,j)
                self.permuteHelper(i+1,nums,result)
                self.swap(nums,i,j)


    def swap(self,arr,i,j):
        arr[i],arr[j] = arr[j],arr[i]