class Solution:
    def reverseWords(self, s: str) -> str:
        # c = [c for c in s]
        c = [s[0]]
        for i in range(1,len(s)):
            if s[i] ==" " and s[i-1]== " ":
                continue
            c.append(s[i])
            
        self.reverse_char(c,0,len(c) - 1)
        
        start_of_word = 0
        
        while start_of_word < len(c):
            end_of_word = start_of_word
            while end_of_word < len(c) and c[end_of_word] != " ":
                end_of_word += 1
            self.reverse_char(c,start_of_word,end_of_word - 1)
            start_of_word = end_of_word + 1
        return "".join(c).strip()
        
    
    def reverse_char(self,char_list,start,end):
        while start < end:
            char_list[start], char_list[end] = char_list[end],char_list[start]
            start += 1
            end -= 1
            