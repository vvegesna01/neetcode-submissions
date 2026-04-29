# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        newList = head = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                print("added from list1")
                print("newList.val", newList.val)
                newList.next = list1
                list1 = list1.next
            else:
                print("added from list2")
                print("newList.val", newList.val)
                newList.next = list2
                list2 = list2.next
            
            newList = newList.next

        newList.next = list1 or list2
        
        return head.next
