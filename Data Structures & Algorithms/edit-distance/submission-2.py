class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prevRow = [j for j in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            curRow = [0 for _ in range(len(word2) + 1)]
            curRow[0] = i

            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    curRow[j] = prevRow[j - 1]
                else:
                    replace = 1 + prevRow[j - 1]
                    add = 1 + curRow[j - 1]
                    remove = 1 + prevRow[j]
                    curRow[j] = min(replace, add, remove)

            prevRow = curRow

        return prevRow[-1]