public class longestCommonPrefixSolu{
    public  String longestCommonPrefix(String[] strs) {
        int len = strs.length;
        if(len == 0){
            return "";
        }
        int minlen = Integer.MAX_VALUE;
        StringBuilder result = new StringBuilder("");
        for(int i = 0;i < len;i++){
            if(strs[i].length()<minlen){
                minlen = strs[i].length();
            }
        }
        for(int i = 0;i<minlen;i++){
            char a = strs[0].charAt(i);
            int j = 0;
            for( j = 1;j < len;j++){
                if(strs[j].charAt(i)!=a){
                    break;
                }
            }
            if(j==len){
                result.append(a);
            }
            else{
                break;
            }
        }
        return result.toString();
    }
}