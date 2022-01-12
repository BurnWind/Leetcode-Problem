# 两数相加：https://leetcode-cn.com/problems/add-two-numbers/
# **(主要是知道怎么去写，逻辑不难)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = cur = ListNode()
        carry = val = 0
        while carry or l1 or l2:
            val = carry
            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val
            carry, val = divmod(val, 10)
            cur.next = ListNode(val)
            cur = cur.next
        return head.next
