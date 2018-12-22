public class largestRectangleAreaSol{
        // this solution is poor, time complexity O(n^2)
    // space complexity O(n)
    public int largestRectangleArea(int[] heights) {
        if(heights.length!=0){
        int[] tmp = new int[heights.length];
        int length = heights.length;
        for(int i = 0;i < length;i++){
            int j = i;
            int k = i;
            while(j>=0&&heights[j]>=heights[i]){
                j--;
            }
            while (k<length&&heights[k]>=heights[i]){
                k++;
            }
            tmp[i] = heights[i]*(k-j-1);
        }
        int max = 0;
        for(int k:tmp){
            if(k>max){
                max=k;
            }
        }
        return max;
        }
        else{
            return 0;
        }
    }
}