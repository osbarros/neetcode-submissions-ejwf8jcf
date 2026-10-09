class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        amountOfEachLetterS = [0 for _ in range(26)]
        for c in s:
            amountOfEachLetterS[ord(c) - ord("a")] += 1

        amountOfEachLetterT = [0 for _ in range(26)]
        for c in t:
            amountOfEachLetterT[ord(c) - ord("a")] += 1
        
        return tuple(amountOfEachLetterS) == tuple(amountOfEachLetterT) 

            
