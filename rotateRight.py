# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # my Solution has time complexity O((k%n)*n) and
        # space complexity O(1).
        # It is easy to optimize the algorithm to time complexity of O(n)
        # while using O(n) space.
        tmp = head
        lenth = 0
        while tmp is not None:
            tmp = tmp.next
            lenth += 1
        if lenth == 0 or k == 0:
            return head
        else:
            k %= lenth
            count = 0
            while count < k:
                tmp = head
                tmp1 = head.val
                while tmp.next is not None:
                    tmp = tmp.next
                    tmp2 = tmp.val
                    tmp.val = tmp1
                    tmp1 = tmp2
                head.val = tmp1
                count += 1
            return head