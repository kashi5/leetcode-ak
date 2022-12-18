class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        if not word:
            return 0
        time = keyboard.find(word[0])
        
        for i in range(1,len(word)):
            travel_time = abs(keyboard.find(word[i-1]) - keyboard.find(word[i]))
            time += travel_time
        
        return time
        