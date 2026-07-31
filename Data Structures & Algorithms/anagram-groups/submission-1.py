class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        
        for s in strs:
            anagramId = [0] * 26
            for c in s:
                anagramId[ord(c) - ord('a')] += 1
            hashableAnagramId = tuple(anagramId)
            if hashableAnagramId not in anagrams:
                anagrams[hashableAnagramId] = [s]
            else: 
                anagrams[hashableAnagramId].append(s)


        
        return list(anagrams.values())
