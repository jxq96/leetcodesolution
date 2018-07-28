public class removeNthFromEndSol{
    class ListNode{
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode start = head;
        ListNode end = head;
        int i = 0;
        while(i<n){
            i++;
            end = end.next;
            
        }
        if(end == null){
                return head.next;
            } 
        end = end.next;
        while(end!=null){
            end = end.next;
            start = start.next;
        }
        start.next = start.next.next;
        return head;
    }
}