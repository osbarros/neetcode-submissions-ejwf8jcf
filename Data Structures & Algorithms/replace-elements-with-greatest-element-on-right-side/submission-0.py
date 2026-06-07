class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curGreatest = 0
        for i in range(len(arr)-1, -1, -1):
            element = arr[i]
            print(f"index: {i}, element: {element}, curGreatest: {curGreatest}")
            arr[i] = curGreatest
            curGreatest = max(curGreatest, element)

        arr[len(arr) - 1] = -1
        return arr
            