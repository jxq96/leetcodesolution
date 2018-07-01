public class isMatchClass{
    public static boolean isMatch(String s,String p){
        int len2 = p.length();
        int len1 = s.length();
       if(len2 == 0){
           return (len1==0);
       }
       else if(len2 == 1){
           if(len1!=1){
               return false;
           }
           else{
               return (s.charAt(0)==p.charAt(0)||p.charAt(0)=='.');
           }
       }
       else{
           if(p.charAt(1)!='*'){
               if(len1==0){
                   return false;
               }
               else{
                   return ((s.charAt(0)==p.charAt(0)||p.charAt(0)=='.')&&isMatch(s.substring(1), p.substring(1)));
               }
           }
           else{
               while(s.length() > 0 && (s.charAt(0)==p.charAt(0)||p.charAt(0)=='.')){
                   if(isMatch(s, p.substring(2))) return true;
                   else{
                       s = s.substring(1);
                   }
               }
               return isMatch(s, p.substring(2));
           }
       }
}
}