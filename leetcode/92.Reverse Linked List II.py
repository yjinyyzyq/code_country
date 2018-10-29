# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next or m >= n or m < 0 or n < 0:
            return head
        count = 1
        pre, cur = None, head
        while cur != None and count < m:
            pre = cur
            cur = cur.next
            count += 1

        t1 = pre
        t2 = cur
        while count <= n and cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
            count += 1
        if m == 1:
            t2.next = cur
            return pre

        t1.next = pre
        t2.next = cur
        return head
