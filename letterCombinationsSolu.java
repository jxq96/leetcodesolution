import java.util.ArrayList;
import java.util.List;
public class Solution{
    public static List<String> letterCombinations(String digits) {
        int len = digits.length();
        StringBuilder tmp = new StringBuilder();
        List<String> result = new ArrayList<>();
        if(len == 0){
            return result;
        }
        int chars;
            if(digits.charAt(0) == '7'||digits.charAt(0)=='9'){
                chars = 4;
            }
            else{
                chars = 3;
            }
           for(int j = 0;j < chars;j++){
                set(0,j,result,len-1,tmp,digits);
                tmp.deleteCharAt(0);
            }
        return result;
    }
    public static void  set(int i,int j,List<String> result,int n,StringBuilder s,String digits){
        if(i==n){
            s.append(map(digits.charAt(i)-'2',j));
            result.add(s.toString());
        }
        else{
            s.append(map(digits.charAt(i)-'2',j));
            int chars;
            if(digits.charAt(i+1)=='7'||digits.charAt(i+1)=='9'){
                chars = 4;
            }
            else{
                chars = 3;
            }
            for(int k = 0;k < chars;k++){
                set(i+1,k,result,n,s,digits);
                s.deleteCharAt(i+1);
            }
        }
    }
    public static char map(int i,int j){
        if(i>=0&&i<=5){
            return (char)('a'+i*3+j);
        }
        else{
            return (char)('a'+i*3+j+1);
        }
    }
    public static void main(String[] args) {
        List<String> result = new ArrayList<>();
        String test = "8";
        result = letterCombinations(test);
        for(int i = 0;i<result.size();i++){
            System.out.println(result.get(i));
        }
    }
}