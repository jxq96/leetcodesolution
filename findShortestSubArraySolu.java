public class findShortestSubArraySolu{
    public int findShortestSubArray(int[] nums) {
        if(nums.length == 0) return 0;
        int max = 1;
        int min = 50000;
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, Integer> firstPoint = new HashMap<>();
        HashMap<Integer, Integer> lastPoint = new HashMap<>();
        List<Integer> list = new ArrayList<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i])){
                map.replace(nums[i], map.get(nums[i])+1);
                lastPoint.replace(nums[i], i);
                if(map.get(nums[i]) > max)
                    max = map.get(nums[i]);
            }
            else{
                map.put(nums[i], 1);
                firstPoint.put(nums[i], i);
                lastPoint.put(nums[i], i);
            }           
        }
        for(Integer it : map.keySet()){
            if(map.get(it).equals(max))
                list.add(it);
        }
        for(Integer it : list){
            int a = lastPoint.get(it) - firstPoint.get(it) + 1;
            min = a > min ? min : a;
        }       
        return min;         
    }
}