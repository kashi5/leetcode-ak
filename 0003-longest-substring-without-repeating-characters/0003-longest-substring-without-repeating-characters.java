import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int startIdx = 0;
        int[] longest = {0,1};
        if (s.length() == 0) return 0;
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        for(int i=0; i<s.length();i++){
            if(map.containsKey(s.charAt(i))){
                startIdx = Math.max(startIdx,map.get(s.charAt(i))+1);
            }
            if (longest[1]-longest[0]<i+1 - startIdx){
                longest = new int[] {startIdx , i+1 };
            }
            map.put(s.charAt(i),i);
        }
        return longest[1]-longest[0];
        
    }
}