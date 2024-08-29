# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        digit = 1
        node = l1
        while True:
            n1 = n1 + node.val * digit
            digit = 10 * digit
            if node.next is None:
                break
            node = node.next
        digit = 1
        node = l2
        while True:
            n2 = n2 + node.val * digit
            digit = 10 * digit
            if node.next is None:
                break
            node = node.next
        s = n1 + n2
        res = ListNode()
        node = res
        while True:
            node.val = s % 10
            s = s // 10
            if s != 0:
                node.next = ListNode()
                node = node.next
            else:
                break
        return res