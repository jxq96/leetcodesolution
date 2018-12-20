public class deleteDuplicatesSol2{
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
    public static ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null){
            return head;
        }
        else{
            ListNode tmp1 = head;
            ListNode tmp2 = tmp1.next;
            while(tmp2!=null){
                if(tmp1.val==tmp2.val){
                    tmp2=tmp2.next;
                    tmp1.next=tmp2;
                }
                else{
                    tmp1=tmp1.next;
                    tmp2=tmp2.next;
                }
            }
            return head;
        }
    }
}