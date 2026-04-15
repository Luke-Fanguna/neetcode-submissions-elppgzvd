# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 

        tmp = head
        dummy = ListNode(tmp.val, None)
        tmp = tmp.next
        while tmp:
            newNode = ListNode(tmp.val, dummy)
            dummy = newNode
            tmp = tmp.next
        return dummy