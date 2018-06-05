import java.util.ArrayList;
import java.util.List;
public class  NQueens1{
    public List<List<String>> solveNQueens(int n){
        int[] QueenSet = new int[n+1];
        List<List<String>> answer = new ArrayList<>();
        place(1, answer, n, QueenSet);
        return answer;
    }

    boolean set(int k ,int[] queen){
        int c =1;
        while(c<k){
            if(queen[c]==queen[k]||Math.abs(k-c)==Math.abs(queen[k]-queen[c]))
            return false; 
            c++;
        }
        return true;
    }
    void place(int k,List<List<String>> ans,int n,int[]queen){
        if(k>n){
            List<String> tmp = new ArrayList<>();
            for(int i=1;i<=n;i++){
                StringBuffer s = new StringBuffer();
                for(int j =1;j<=n;j++){
                    if(j==queen[i]){
                        s.append("Q");
                    }
                    else{
                        s.append(".");
                    }
                }
                tmp.add(s.toString());
            }
            ans.add(tmp);
        }
        else {
            for(int j =1;j<=n;j++){
                queen[k] = j;
                if(set(k, queen)){
                    place(k+1, ans, n, queen);
                }
            }
        }
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<String>> l = s.solveNQueens(4);
        int n = l.size();
        for(int i=0;i<n;i++){
            for(int j=0;j<4;j++){
                System.out.println(l.get(i).get(j));
            }
            System.out.print("\n");
        }
    }
}