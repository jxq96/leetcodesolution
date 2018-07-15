public class fourSumSolu{
    public  List<List<Integer>> fourSum(int[] nums, int target) {
        if(nums==null||nums.length<4){
            return new ArrayList<List<Integer>>();
        }
        else{
            List<List<Integer>> result = new ArrayList<>();
            Arrays.sort(nums);
            int len = nums.length - 3;
            int tmplen = len + 3;
            for(int i = 0;i<len;i++){
                List<List<Integer>> tmpList = threeSum(nums, target-nums[i],i+1,tmplen);
                if(tmpList.size()!=0){
                    int size = tmpList.size();
                    for(int k = 0;k<size;k++){
                        List<Integer> temp = tmpList.get(k);
                        temp.add(nums[i]);
                        result.add(temp);
                        
                    }
                }
                while(i<len&&nums[i+1] == nums[i]){
                    i++;
                }
            }
            return result;
        }
    }
    public List<List<Integer>> twoSum(int[] nums,int target,int begin,int end){
        if(end <= begin){
            return null;
        }
        else{
            List<List<Integer>> result = new ArrayList<List<Integer>>();
            int i = begin;
            int j = end;
            while(i < j){
                int check = nums[i] + nums [j];
                if(check== target){
                    List<Integer> temList = new ArrayList<Integer>();
                    temList.add(nums[i]);
                    temList.add(nums[j]);
                    result.add(temList);
                    while(i < end && nums[i+1] == nums[i]) i++;
                    while(j > begin&& nums[j-1] == nums[j]) j--;
                    List<List<Integer>> temList2 = twoSum(nums,target,++i,--j);//递归，很自然的想法
                    if(temList2 != null&&temList2.size()!=0){
                        int size = temList2.size();
                        for(int k = 0;k < size;k++){
                            List<Integer> temp = temList2.get(k);
                            result.add(temp);
                        }
                    }
                    break;
                }
                else if(check < target){
                    i++;
                }
                else{
                    j--;
                }
            }
            return result;
        }
    }
    public List<List<Integer>> threeSum(int[] nums,int target,int begin,int end) {
        if(nums == null || nums.length < 3){
            return new ArrayList<List<Integer>>();
        }
        else{
            List<List<Integer>> result = new ArrayList<List<Integer>>();
            int len = end - 2;
            for(int i = begin; i < len;i++){
                List<List<Integer>> temList = twoSum(nums,target - nums[i],i + 1,len + 1);
                if(temList!=null&&temList.size()!=0){
                    int size = temList.size();
                    for(int k = 0;k < size;k++){
                        List<Integer> tempList2 = temList.get(k);
                        tempList2.add(nums[i]);
                        result.add(tempList2);
                    }
                }
                while(i<len&&nums[i+1] == nums[i]){
                    i++;
                }
            }
            return result;
        }

    }
}