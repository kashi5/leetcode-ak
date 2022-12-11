class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                if s_dict[s[i]]==t[i]:
                    continue
                else:
                    return False
            if t[i] in s_dict.values():
                return False
            s_dict[s[i]]=t[i]
        
        return True
        