public class threeSumClosestSolu{
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int i = 0;
        while(true){
            if(threeSum(nums, target+i)){
                return target + i;
            }
            if(threeSum(nums, target-i)){
                return target - i;
            }
            i++;
        }
    }
    public boolean twoSum(int[] nums,int target,int begin,int end){
        if(end <= begin){
            return false;
        }
        else{
            int i = begin;
            int j = end;
            while(i < j){
                int check = nums[i] + nums [j];
                if(check== target){
                    return true;
                }
                else if(check < target){
                    i++;
                }
                else{
                    j--;
                }
            }
            return false;
        }
    }
    public boolean threeSum(int[] nums,int target) {
        if(nums == null || nums.length < 3){
            return false;
        }
        else{
            //Arrays.sort(nums);
            int len = nums.length - 2;
            for(int i = 0; i < len;i++){
                 boolean two= twoSum(nums, target-nums[i],i + 1,len + 1);
                 if(two){
                     return true;
                 }
                while(i<len&&nums[i+1] == nums[i]){
                    i++;
                }
            }
            return false;
        }

    }
}