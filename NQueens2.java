public class NQueens2{
    public int totalNQueens(int n) {
        int[] count = {0};
        int[] Queenset = new int[n+1];
        place(1, n, Queenset, count);
        return count[0];        
    }
    void place(int i,int n,int[]set,int[] count){
        if(i>n){
            count[0]++;
        }
        else{
            for(int j = 1;j<=n;j++){
                set[i] = j;
                if(isvalid(i, set)){
                    place(i+1, n, set, count);
                }
            }
        }
}
 boolean isvalid(int i,int[]set){
    int c =1;
    while(c<i){
        if(set[c]==set[i]||Math.abs(i-c)==Math.abs(set[i]-set[c]))
        return false; 
        c++;
    }
    return true;
 }
}