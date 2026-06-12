class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_s = len(s)
        i = 0

        for c in t:
            if i < length_s and c == s[i]:
                i += 1


        return i == length_s