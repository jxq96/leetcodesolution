public class findLengthOfLCISSolu{
    public int findLengthOfLCIS(int[] nums) {
        int count = 1;
        int max = 1;
        int len = nums.length;
        if(len == 0){
            return 0;
        }
        else{
        for(int i = 1;i<len;i++){
            if(nums[i]>nums[i-1]){
                count++;
            }
            else{
                count = 1;
            }
            if(count>max){
                max = count;
            }
        }
        return max;
    }
    }
}