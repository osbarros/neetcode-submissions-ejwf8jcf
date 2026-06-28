# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr = slow
        prev = None
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        
        maxSum = 0
        slow = prev

        while slow:
            maxSum = max(maxSum, slow.val + head.val)
            slow = slow.next
            head = head.next
        
        return maxSum
    
               

        
            

        

        