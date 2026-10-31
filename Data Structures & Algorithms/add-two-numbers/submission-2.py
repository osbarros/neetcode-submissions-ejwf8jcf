# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3Dummy = ListNode()
        l3 = ListNode()
        l3Dummy.next = l3
        digit = 0 
        carry = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0 

            total = val1 + val2 + carry

            digit = total % 10 
            carry = total // 10

            l3.val = digit

            if l1:
                l1 = l1.next
            
            if l2:
                l2 = l2.next

            if l1 or l2:
                l3.next = ListNode()
                l3 = l3.next

        
        if carry > 0:
            l3.next = ListNode(carry)



        return l3Dummy.next

        