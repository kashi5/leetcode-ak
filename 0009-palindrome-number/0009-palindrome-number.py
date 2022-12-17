class Solution:
    def isPalindrome(self, x: int) -> bool:
        #11211
        y = str(x)
        start = 0
        end = len(y) - 1
        while start < end :
            if y[start] != y[end]:
                return False
            start += 1
            end -= 1
        return True
            
        