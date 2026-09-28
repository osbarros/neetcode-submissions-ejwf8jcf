class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        curRow = [0 for _ in range(len(text1) + 1)]
        prevRow = curRow.copy()

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text1[j - 1] == text2[i - 1]:
                    curRow[j] = 1 + prevRow[j - 1]
                else:
                    curRow[j] = max(curRow[j - 1], prevRow[j])
            prevRow = curRow.copy()

        return curRow[len(text1)]