class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curPrefix = ""

        minLen = min(len(s) for s in strs)

        for i in range(minLen):
            for s in strs:
                if s[i] != strs[0][i]:
                    return curPrefix            
            curPrefix += strs[0][i]

        return curPrefix
