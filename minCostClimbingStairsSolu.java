public class minCostClimbingStairsSolu{
    public int minCostClimbingStairs(int[] cost) {
        int len = cost.length;
        if(len == 2){
            return Math.min(cost[0], cost[1]);
        }
        else{
        int[] tmp = new int[cost.length + 1];
        tmp[0] = 0;
        tmp[1] = 0;
        for(int i = 2;i<=len;i++){
            tmp[i] = tmp[i-2]+cost[i-2]<tmp[i-1]+cost[i-1]?tmp[i-2]+cost[i-2]:tmp[i-1]+cost[i-1];
        }
        return tmp[len];
     }   
 }
}