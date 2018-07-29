public class mergeTwoListsSol{
    class ListNode{
        int val;
        ListNode next;
        ListNode(int x){val = x;};
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
      if(l1==null){
          return l2;
      }
      if(l2 == null){
          return l1;
      }
      ListNode result;
      if(l1.val<=l2.val){
          result = l1;
          l1 = l1.next;
      }
      else{
          result = l2;
          l2 = l2.next;
      }
      ListNode tmp = result;
      while(l1!=null&&l2!=null){
          if(l1.val<=l2.val){
              tmp.next = l1;
              l1 = l1.next;
          }
          else{
              tmp.next = l2;
              l2 = l2.next;
          }
          tmp = tmp.next;
      }
      if(l1!=null){
          tmp.next = l1;
      }
      if(l2!=null){
          tmp.next = l2;
      }
      return result;
 }
}