public class myAtoiSolu{
    public static int myAtoi(String str){
        StringBuffer num = new StringBuffer();
        boolean flag = false;
        if(str.length()==0){
            return 0;
        }
       else if(str.charAt(0)!='+'&&str.charAt(0)!=' '&&str.charAt(0)!='-'&&!(str.charAt(0)>='0'&&str.charAt(0)<='9')){
            return 0;
        }
        else{
            int i =0;
            while(str.charAt(i)==' '){
                i++;
                if(i==str.length()){
                    return 0;
                }
            }
            if(str.charAt(i)=='+'){
                flag = false;
                i++;
                if(i==str.length()){
                    return 0;
                }
                while(str.charAt(i)=='0'){
                    i++;
                    if(i==str.length()){
                        return 0;
                    }
                }          
                if(!(str.charAt(i)>'0'&&str.charAt(i)<='9')){
                    return 0;
                }
            }
            else if(str.charAt(i)=='-'){  
                    flag = true;
                    i++;    
                    if(i==str.length()){
                        return 0;
                    }       
                    while(str.charAt(i)=='0'){
                        i++;
                        if(i==str.length()){
                            return 0;
                        }
                    }
                }
                else if(str.charAt(i)=='0'){
                    flag = false;
                    while(str.charAt(i)=='0'){
                        i++;
                    if(i==str.length()){
                        return 0;
                    }
                }
                }
                while(str.charAt(i)>='0'&&str.charAt(i)<='9'){
                    num.append(str.charAt(i));
                    i++;  
                    if(i==str.length()){
                        break;
                    }
                }
                int len = num.length();
                if(len == 0){
                    return 0;
                }
                //tring tmps = num.toString();
                if(len<10){
                    return s2i(num.toString(), flag);
                }
                else{
                    if(flag){
                        if(len>10){
                        return Integer.MIN_VALUE;
                        }
                        else{
                            String tmp = "2147483648";
                            for(int j =0;j<10;j++){
                                if(num.charAt(j)>tmp.charAt(j)){
                                    return Integer.MAX_VALUE;
                                }
                                else if(num.charAt(j)<tmp.charAt(j)){
                                    return s2i(num.toString(), flag);
                                }
                            }
                            return Integer.MIN_VALUE;
                        }
                    }
                    else{
                        if(len>10){
                        return Integer.MAX_VALUE;
                        }
                        else{
                            String tmp = "2147483647";
                            for(int j =0;j<10;j++){
                                if(num.charAt(j)>tmp.charAt(j)){
                                    return Integer.MAX_VALUE;
                                }
                                else if(num.charAt(j)<tmp.charAt(j)){
                                    return s2i(num.toString(), flag);
                                }
                            }
                            return Integer.MAX_VALUE;
                        }
                    }
                }
                
            }
            
        } 
    
    
    public static int s2i(String str,boolean flag){
        int result = 0;
        int len = str.length();
        result = str.charAt(0)-'0';
        for(int i =1;i<len;i++){
            result=result*10+str.charAt(i)-'0';
        }
        return flag?(-1*result):result;       
    }

    public static void main(String[] args) {
        int a = myAtoi("-2");
        int b =myAtoi("+2");
        int c = myAtoi("ada121");
        int d =myAtoi("  +001313");
        int e =myAtoi("  -1102");
        int f = myAtoi("-002434");
        int g =myAtoi("144141414141");
        int h = myAtoi("  002147483647");
        int i = myAtoi("-002147483648");
        int j =myAtoi("-");
        int k =myAtoi(" ");
        int l = myAtoi("    0000000000000  ");
        int m = myAtoi("000000000000000000000000000011");
        int n =myAtoi("2147483648");
         //System.out.println(myAtoi("-"));
         //System.out.println(myAtoi(" "));
        System.out.print(myAtoi("-2"));
        //System.out.println(myAtoi("+"));
        System.out.println(myAtoi("+2"));
        System.out.println(myAtoi("afafa1141"));
        System.out.println(myAtoi("  000012313"));
        System.out.println(myAtoi("   -0002147483648"));
        System.out.println(myAtoi("+0002147483647"));
        System.out.println(myAtoi("2147483647"));
        System.out.println(myAtoi("-00123"));
        System.out.println(myAtoi("+00123"));

    }
}
