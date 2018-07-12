public class subsetsSolu{
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        result.add(new ArrayList<Integer>());
        int len = nums.length;
        for(int i = 0;i<len;i++){
            int size = result.size();
            for(int j = 0;j<size;j++){
                List<Integer> tmp = new ArrayList<Integer>(result.get(j));
                tmp.add(nums[i]);
                result.add(tmp);
            }
        }
        return result;
     }  
}