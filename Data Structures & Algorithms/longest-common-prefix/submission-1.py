class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curPrefix = ""

        minLen = min(len(s) for s in strs)

        for i in range(minLen):
            for k, s in enumerate(strs):
                if s[i] != strs[0][i]:
                    return curPrefix
                previous = s[i]
            
            curPrefix += strs[0][i]

        return curPrefix

                

            