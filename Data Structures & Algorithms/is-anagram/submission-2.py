class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        contentString = set()
        amountOfEachLetter = [0 for _ in range(26)]
        for c in s:
            amountOfEachLetter[ord(c) - ord("a")] += 1
        contentString.add(tuple(amountOfEachLetter))


        amountOfEachLetter = [0 for _ in range(26)]
        for c in t:
            amountOfEachLetter[ord(c) - ord("a")] += 1
        
        return tuple(amountOfEachLetter) in contentString

            
