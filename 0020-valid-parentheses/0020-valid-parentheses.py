class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket_string="({["
        close_bracket_string = ")}]"
        matching_brackets = {")":"(","}":"{","]":"["}
        stack = []
        for char in s:
            if char in open_bracket_string:
                stack.append(char)
            elif char in close_bracket_string:
                if len(stack) == 0:
                    return False
                if stack[-1] == matching_brackets[char]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
                
                
            
        
    