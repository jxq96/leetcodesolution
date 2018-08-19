# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        else:
            tmphead = head
            tmpmove = head
            flag = True
            count = 1
            result = head
            prev = None
            while tmpmove is not None and count < k:
                tmpmove = tmpmove.next
                count = count + 1
                if count == k and tmpmove is not None:
                    tmp = tmpmove.next
                    if flag:
                        result = self.reverse(tmphead, tmpmove)
                        prev = tmphead
                        prev.next = tmp
                        tmphead = tmp
                        tmpmove = tmp
                        count = 0
                        flag = False
                    else:
                        prev.next = self.reverse(tmphead, tmpmove)
                        prev = tmphead
                        prev.next = tmp
                        tmphead = tmp
                        tmpmove = tmp
                        count = 0
            return result
    def reverse(self, head, tail):
        prev = head
        now = head.next
        while prev != tail:
            then = now.next
            now.next = prev
            prev = now
            now = then
        head.next = None
        return tail

