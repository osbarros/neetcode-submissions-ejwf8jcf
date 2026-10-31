# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        prevL1 = None
        lenL1 = 0
        while l1:
            tmp = l1.next
            l1.next = prevL1 
            prevL1 = l1
            l1 = tmp
            lenL1 += 1



        head = prevL1


        multiplier = 10 ** (lenL1 -1)
        numberL1 = 0
        while head:
            numberL1 += head.val * multiplier
            multiplier = multiplier // 10
            head = head.next

        #L2

        prevL2 = None
        lenL2 = 0
        while l2:
            lenL2 += 1
            tmp = l2.next
            l2.next = prevL2 
            prevL2 = l2
            l2 = tmp

        head = prevL2

        multiplier = 10 ** (lenL2 -1)
        numberL2 = 0
        while head:
            numberL2 += head.val * multiplier
            multiplier = multiplier // 10
            head = head.next

        additionNumber = numberL1 + numberL2

        additionStr = str(additionNumber)

        outputHeadDummy = ListNode()

        curr = ListNode()

        outputHeadDummy.next = curr


        for i in range(len(additionStr) - 1, -1, -1):
            curr.val = int(additionStr[i])
            if i != 0:
                curr.next = ListNode()
                curr = curr.next


        return outputHeadDummy.next


            



        
    
            
            