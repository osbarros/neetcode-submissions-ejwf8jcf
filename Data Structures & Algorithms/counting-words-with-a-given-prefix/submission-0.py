class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        output = 0
        for word in words:

            contains = False
            for i in range(len(pref)):
                if word[i] != pref[i]:
                    break
                else:
                    if i == len(pref) - 1:
                        contains = True
                
            if contains:
                output += 1


        return output
                    
        