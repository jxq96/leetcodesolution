public class isScrambleSol{
    public boolean isScramble(String s1, String s2) {
        if(s1.length()!=s2.length()){
            return false;
        }
        else{
            char[] list1 = s1.toCharArray();
            char[] list2 = s2.toCharArray();
            Arrays.sort(list1);
            Arrays.sort(list2);
            if(!Arrays.equals(list1,list2)){
                return false;
            }
            int len = s1.length();
            if(len==1){
                return s1.charAt(0) == s2.charAt(0);
            }
            else if(len==2){
                return (s1.charAt(0)== s2.charAt(0) && s1.charAt(1)==s2.charAt(1))||
                        (s1.charAt(1)== s2.charAt(0) && s1.charAt(0)==s2.charAt(1));
            }
            for(int i = 1;i<len;i++){
                if(isScramble(s1.substring(0,i),s2.substring(0,i))&&isScramble(s1.substring(i),s2.substring(i))){
                    return true;
                }
                if(isScramble(s1.substring(0,i),s2.substring(len-i))&&isScramble(s1.substring(i),s2.substring(0,len-i))){
                    return true;
                }
            }
            return false;
        }
    }
}