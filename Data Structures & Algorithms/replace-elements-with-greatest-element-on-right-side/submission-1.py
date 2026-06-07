class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curGreatest = 0
        for i in range(len(arr)-1, -1, -1):
            old = arr[i]
            arr[i] = curGreatest
            curGreatest = max(curGreatest, old)

        arr[len(arr) - 1] = -1
        return arr
            