class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None or m >= n or m <= 0 or n <= 0:
            return head
        else:
            i = 1
            t1 = head
            t2 = head
            while i < m and t2 is not None:
                t1 = t2
                t2 = t2.next
                i += 1
            t3 = t2
            t4 = t2.next
            t5 = t4.next
            while i < n and t4 is not None:
                t4.next = t3
                t3 = t4
                t4 = t5
                if t4 is None:
                    break
                t5 = t4.next
                i += 1
            if m != 1:
                t1.next = t3
                t2.next = t4
                return head
            else:
                t2.next = t4
                return t3