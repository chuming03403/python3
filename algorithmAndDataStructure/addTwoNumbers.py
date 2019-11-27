# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        两个链表相加，链表顺序为低位到高位
        https://leetcode-cn.com/problems/add-two-numbers
        """
        carry = 0;
        result = root = ListNode(0);
        while l1 or l2 or carry:
            v1 = v2 = 0;
            if l1:
                v1 = l1.val;
                l1 = l1.next;
            if l2:
                v2 = l2.val;
                l2 = l2.next;
            carry, val = divmod(v1 + v2 + carry, 10);
            result.next = ListNode(val);
            result = result.next;
        return root.next;