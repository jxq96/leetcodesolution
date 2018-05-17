public class Solution{
    public static int reverse(int x){
        if(x<10&&x>-10){
            return x;
        }
        int y = 0;
        boolean flag = false;
        if(x<0){
            flag = true;
            x = -1*x;
        }
        int remain;
        int step = 10;
        while(x!=0){
            remain = x%10;
            y = y*step+remain;            
            x = x/10;
            if(x!=0&&y>Integer.MAX_VALUE/10){
                return 0;
            }
        }
       if(flag){
           y = -1*y;
           if(y>=0){
               return 0;
           }
           else{
               return y;
           }
       }
       else{
           if(y<=0){
               return 0;
           }
           else{
               return y ;
           }
       }
    }
    
}