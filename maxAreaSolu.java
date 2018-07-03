public class maxAreaSolu{
    public  int maxArea(int[] height) {
        int len = height.length;
        int i = 0;
        int j = len - 1;
        max = calculate(i, j, height[i], height[j]);
        while(i<j){
            if(height[i]<height[j]){
                i++;
            }
            else{
                j--;
            }
            int area = calculate(i, j, height[i], height[j]);
                max = (max>area)?max:area;
        }
        return max;
    }
    public int calculate(int i,int j,int hi,int hj){
        int lower = (hi>hj)?hj:hi;
        return (j-i)*lower;
    }
}