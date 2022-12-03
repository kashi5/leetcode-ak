class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using in build sort method, very naive approch to solve the problem (nlogn)
        # nums.sort()
        # return nums[-k]
        
        # Hoare algorithm O(n)
        position = len(nums) - k
        start = 0
        end = len(nums) - 1
        
        while True:
            if start > end:
                raise Exception("error")
            left = start + 1
            right = end
            pivot = start
            while left <= right:
                if nums[pivot] < nums[left] and nums[pivot] > nums[right]:
                    self.swap(nums,left,right)
                if nums[pivot] >= nums[left]:
                    left += 1
                if nums[pivot] <= nums[right]:
                    right -= 1
            self.swap(nums,pivot,right)
            if position == right:
                return nums[right]
            elif position > right :
                start = right + 1
            else:
                end = right - 1
            
    
    def swap(self, nums,l,r):
        nums[l],nums[r]=nums[r],nums[l]
                