public class mergeKListsSol{
    class ListNode{
        int val;
        ListNode next;
        ListNode(int x){
            val = x;
        }
    }
    public ListNode mergeKLists(ListNode[] lists) {
        int number = lists.length;
        ListNode result,tmp;
        int index = indexOfMin(lists, number);
        if(index==number){
            return null;
        }
        else{
            result = lists[index];
            tmp = result;
            lists[index] = lists[index].next;
        }
        while(true){
            index = indexOfMin(lists, number);
            if(index==number){
                break;
            }
            else{
                tmp.next = lists[index];
                tmp = tmp.next;
                lists[index]=lists[index].next;
            }
        }
        return result;
    }
    int indexOfMin(ListNode[] lists,int number){
        int result = number;
        int j;
        for(j = 0;j<number;j++){
            if(lists[j]!=null){
                result = j;
                break;
            }
        }
        if(result!=number){
        for(int k = j;k<number;k++){
            if(lists[k]!=null){
                if(lists[k].val<lists[result].val){
                    result = k;
                }
            }
        }
    }
        return result;
    }
}