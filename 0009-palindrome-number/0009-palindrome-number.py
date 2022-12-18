class Solution:
    def isPalindrome(self, x: int) -> bool:
        #11211
        # y = str(x)
        # start = 0
        # end = len(y) - 1
        # while start < end :
        #     if y[start] != y[end]:
        #         return False
        #     start += 1
        #     end -= 1
        # return True
        
        if x<0 or x%10 == 0 and  x!=0 :
            return False
        
        rev_num = 0
        
        while x> rev_num:
            rev_num = rev_num * 10 + x%10
            x //= 10
            
        return x == rev_num or x == rev_num//10
        
        