public class searchMatrixSolu{
    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        if(rows == 0){
            return false;
        } 
        else{
            int column = matrix[0].length;
            return search(matrix, target, 0, rows-1,column);
        }
     }
 
     public boolean search(int[][]matrix,int target,int start,int end,int column){
         if(start>end||column==0){
             return false;
         }
         else{
             int m = (start+end)/2;
             if((target>=matrix[m][0]&&target<=matrix[m][column-1])){
                 for(int i = 0;i<column;i++){
                     if(matrix[m][i]==target){
                         return true;
                     }
                 }
                 return false;
             }
             else if(target<matrix[m][0]){
                 return search(matrix, target, 0, m-1, column);
             }
             else{
                 return search(matrix, target, m+1, end, column);
             }
         }
     }
}