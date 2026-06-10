class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        curPrefix = ""

        minLen = min(len(s) for s in strs)

        for i in range(minLen):
            previous = ''
            for k, s in enumerate(strs):
                if previous != '' and s[i] != previous:
                    return curPrefix
                previous = s[i]
            
            curPrefix += strs[0][i]

        return curPrefix

                

            