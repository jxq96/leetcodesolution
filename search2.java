public class search2 {
    public static boolean search(int[] nums,int target){
        int length = nums.length;
        if(length==0){
            return false;
        }
        int i;
        for(i = 0; i < length - 1;i++){
            if(nums[i]==target){
                return true;
            }
            if(nums[i+1] < nums[i]){
                break;
            }
        }
        i++;
        length--;
        int index = (i+length)/2;
        do{
            if(nums[index]==target){
                return true;
            }
            else if(nums[index] < target){
                i = index + 1;
                index = (i+length)/2;
            }
            else{
                length = index - 1;
                index = (i+length)/2;
            }
        }while (i<=length);
        return false;
    }
    public static void main(String[]argv){
        int[] nums = {2,5,6,0,0,1,2};
        int target = 3;
        System.out.println(search(nums,target));
    }
}
