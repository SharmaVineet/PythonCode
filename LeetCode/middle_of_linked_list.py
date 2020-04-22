# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head:
            i = 0
            current = head
            while current:
                current = current.next
                i += 1
            j = 0
            current = head
            while j != i // 2:
                current = current.next
                j += 1
            return current
