public class isPalindrome{
    public boolean isPalindromeSol(int x){
        int tmp = x;
        int remain = 0;
        boolean isnegtive = (x<0)?true:false;
        if(isnegtive){
            return false;
        }
        tmp = x;
        while(tmp>0){
            remain = remain*10+tmp%10;
            tmp = tmp/10;
        }
        if(remain==x){
            return true;
        }
        else{
            return false;
        }
    }
}