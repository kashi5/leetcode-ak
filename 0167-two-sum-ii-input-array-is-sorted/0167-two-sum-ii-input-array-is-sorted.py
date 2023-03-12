class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        my_dict={}
        output = []
        print(numbers)
        for i in range(0,len(numbers)):
            value = target - numbers[i]
            if value in my_dict:
                return [my_dict.get(value),i+1]
            my_dict.update({numbers[i]:i+1})
                