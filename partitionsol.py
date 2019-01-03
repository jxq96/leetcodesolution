class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""

shabby code!
"""
class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return head
        else:
            p = ListNode(-1)  # the initial value is doesn't matter
            p.next = head
            preq = p
            q = head
            while q is not None:
                if q.val < x:
                    if q == head:
                        preq = q
                        p = q
                        q = q.next
                    else:
                        if p.next == head:
                            preq.next = q.next
                            q.next = head
                            head = q
                            p = q
                            q = preq.next
                        else:
                            if p.next != q:
                                preq.next = q.next
                                q.next = p.next
                                p.next = q
                                p = q
                                q = preq.next
                            else:
                                preq = q
                                p = q
                                q = q.next

                else:
                    preq = q
                    q = q.next
            return head