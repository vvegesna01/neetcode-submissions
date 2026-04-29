# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head

        # traverse list to find size
        N = 0
        while cur:
            N += 1
            cur = cur.next
        
        print(N)
        cur = head
        removeIndex = N - n

        if removeIndex == 0:
            return head.next

        for i in range(N - 1):
            if (i+1) == removeIndex:
                cur.next = cur.next.next
                break
            else:
                cur = cur.next
        
        return head
            