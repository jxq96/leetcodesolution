import java.util.Arrays;
public class findUnsortedSubarraySolu{
    public static int findUnsortedSubarray(int[] nums) {
       int i = 0;
       int j = nums.length - 1;
       int len = nums.length;
       int[] tmp = new int[len];
       for(int k =0;k<len;k++){
           tmp[k] = nums[k];
       } 
       Arrays.sort(nums);
       int start = 0,end = -1;
       for(;i<len;i++){
           if(nums[i]!=tmp[i]){
               start = i;
               break;
           }
       }
       for(;j>=0;j--){
           if(nums[j]!=tmp[j]){
               end = j;
               break;
           }
       }
       return end - start +1;
    } 
    public static void main(String[] args) {
        int[] nums = {1,3,2,2,2};
        int result = findUnsortedSubarray(nums);
        System.out.print(result);
    }
}