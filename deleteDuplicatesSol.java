public class deleteDuplicatesSol{
    class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }
  
      public  ListNode deleteDuplicates(ListNode head) {
          if(head==null || head.next==null){
              return head;
          } // no element or one element
          else{ // at least two elements
              while (head!=null&&head.next!=null&&head.val==head.next.val) {
                  while (head.next != null && head.val == head.next.val) {
                      head = head.next;
                  }
                  head = head.next;
              }
              if(head!=null&&head.next!=null){
                  ListNode tmp1 = head;
                  ListNode tmp2 = head.next;
                  while (tmp2!=null&&tmp2.next!=null){
                      if(tmp2.val==tmp2.next.val){
                          int tmp = tmp2.val;
                          while(tmp2!=null){
                              if(tmp2.val==tmp){
                                  tmp2=tmp2.next;
                              }
                              else {
                                  break;
                              }
                          }
                          tmp1.next = tmp2;
                      }
                      else{
                          tmp1=tmp1.next;
                          tmp2 = tmp2.next;
                      }
                  }
              }
              return head;
          }
      }
    }