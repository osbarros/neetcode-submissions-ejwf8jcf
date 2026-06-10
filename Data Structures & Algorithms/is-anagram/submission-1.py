class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}

        if len(s) != len(t):
            return False

        for c in s:
            map_s[c] = map_s.get(c, 0) + 1
        
        for c in t:
            if c in map_s and map_s[c] > 0:
                map_s[c] = map_s[c] - 1
            else: 
                return False
        
        return True
        

