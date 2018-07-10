public class matrixReshapeSolu{
    public static int[][] matrixReshape(int[][] nums, int r, int c) {
        int rini = nums.length;
        int cini = nums[0].length;
        if(rini*cini != r*c){
            return nums;
        }
        else{
            int[] tmp = new int[r*c];
            int[][] result = new int[r][c];
            int k = 0;
            for(int i = 0;i < rini;i++){
                for(int j = 0;j < cini;j++){
                    tmp[k++] = nums[i][j];
                }
            }
            k = 0;
            for(int i = 0;i < r;i++){
                for(int j = 0;j < c;j++){
                    result[i][j] = tmp[k++];
                }
            }
            return result;
        }
    }
    public static void main(String[] args) {
        int[][] nums = {{1,2},{3,4}};
        matrixReshape(nums, 1,4);
    }
}