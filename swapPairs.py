# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            result = head.next
            result.next = head
            head.next = None
            return result
        else:
            first = head
            second = head.next
            result = second
            while True:
                first.next = second.next
                second.next = first
                tmp = first
                first = first.next
                if first is None:
                    break
                else:
                    if first.next is None:
                        break
                    else:
                        second = first.next
                        tmp.next = second
            return result
