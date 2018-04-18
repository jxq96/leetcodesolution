public class longestPalindrome {
    public static String longestPalindrome(String s) {
        int len = s.length();
        int tmplen = len;
        boolean flag;
        while (tmplen > 0) {
            for (int i = 0; i <= len - tmplen; i++) {
                flag = isPalindrome(s,i,i+tmplen-1);
                if(flag){
                    return s.substring(i,i+tmplen);
                }
            }
            tmplen--;
        }
        return s.substring(0,1);
    }

    public static boolean isPalindrome(String s,int i,int j){
        boolean result = true;
        while(i<j){
            if(s.charAt(i)==s.charAt(j)){
                i++;
                j--;
            }
            else {
                result = false;
                break;
            }
        }
        return result;
    }
    public static void main(String[] args){
        java.util.Scanner input = new java.util.Scanner(System.in);
        String test = input.next();
        String result = longestPalindrome(test);
    }
}
