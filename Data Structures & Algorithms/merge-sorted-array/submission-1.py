class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        index1 = m - 1
        index2 = len(nums2) - 1

        i = 1
        while index2 >= 0 and index1 >=0:            
            if nums1[index1] > nums2[index2]: 
                nums1[-i] = nums1[index1]
                index1 -= 1
            else:
                nums1[-i] = nums2[index2]
                index2 -= 1
            i+=1

        while index2 >= 0:
            nums1[index2] = nums2[index2]
            index2 -= 1






        