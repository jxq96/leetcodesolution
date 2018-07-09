public class wordBreakSolu{
    public static boolean wordBreak(String s, List<String> wordDict){
        boolean[] check = new boolean[s.length()+1];
        check[0] = true;
        int strlen = s.length();
        int dicklen = wordDict.size();
        for(int i = 0;i < strlen;i++){
            for(int j = 0;j < dicklen;j++){
                String tmp = wordDict.get(j);
                if(check[i] && tmp.length()+i<=strlen &&s.substring(i,i+tmp.length()).equals(tmp)){
                    check[i+tmp.length()] = true;
                }
            }
        }
        return check[strlen];
    }
}