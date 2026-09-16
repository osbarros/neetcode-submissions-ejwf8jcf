class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            nextPerms = []
            for p in perms:
                for i in range(len(p) + 1):
                    if i > 0 and p[i - 1] == n:
                        break
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    nextPerms.append(pCopy)
            perms = nextPerms
        return perms