class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapT = {}
        mapS = {}

        for i in range(len(s)):
            if s[i] in mapS:
                if mapS[s[i]] != t[i]:
                    return False

            else: 
                mapS[s[i]] = t[i]
            
            if t[i] in mapT:
                if mapT[t[i]] != s[i]:
                    return False

            else:
                mapT[t[i]] = s[i]


        return True