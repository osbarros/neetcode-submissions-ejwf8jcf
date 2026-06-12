class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length_s = len(s)
        count_equals = 0
        i = 0

        for c in t:
            if i < length_s and c == s[i]:
                i += 1
                count_equals += 1

            if count_equals == length_s:
                return True
        
        return False