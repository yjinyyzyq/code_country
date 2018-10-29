# coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 反转一个链表。
        # pre 指向前一个值，没有为Null.
        # cur 指向当前值，就是要操作的值。
        # next 指向当前值的next.
        if not head:
            return
        pre, cur = None, head
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next

        return pre



