# Leetcode 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        current = result = ListNode()

        while l1 is not None or l2 is not None or carry:
            l1_not_none = l1 is not None
            l2_not_none = l2 is not None
            l1_v = l1.val if l1_not_none else 0
            l2_v = l2.val if l2_not_none else 0
            current.val = carry + l1_v + l2_v
            carry = current.val // 10
            current.val %= 10
            print(l1_not_none, l2_not_none, carry)
            if l1_not_none:
                l1 = l1.next
            if l2_not_none:
                l2 = l2.next
            if l1 is not None or l2 is not None or carry:
                current.next = ListNode()
                current = current.next

        return result
