public class romeToIntSolu{
    public in romeToInt(String s){
    int len = s.length();
        int result = 0;
        int i;
        for( i = 0;i < len-1;){
            char a = s.charAt(i);
            char b = s.charAt(i+1);
            if(a=='I'){
                if(b=='V'){
                    result += 4;
                    i = i+2;
                }
                else if(b=='X'){
                    result += 9;
                    i = i+2;
                }
                else{
                    result += 1;
                    i++;
                }
            }
            else if(a=='X'){
                if(b=='L'){
                    result += 40;
                    i = i+2;
                }
                else if(b=='C'){
                    result += 90;
                    i = i+2;
                }
                else{
                    result += 10;
                    i = i+1;
                }
            }
            else if(a=='C'){
                if(b=='D'){
                    result += 400;
                    i = i+2;
                }
                else if(b == 'M'){
                    result += 900;
                    i = i+2;
                }
                else{
                    result +=100;
                    i++;
                }
            }
            else if(a=='V'){
                result+=5;
                i++;
                while(i<len&&s.charAt(i)=='I'){
                    result+=1;
                    i++;
                }
            }
            else if(a=='L'){
                result+=50;
                i++;
                while(i<len&&s.charAt(i)=='X'){
                    result+=10;
                    i++;
                }
            }
            else if(a=='D'){
                result+=500;
                i++;
                while(i<len&&s.charAt(i)=='C'){
                    result+=100;
                    i++;
                }
            }
            else{
                result+=1000;
                i++;
            }
        }
        if(i<len){
            char a = s.charAt(i);
            switch (a) {
                case 'I':result+=1;
                    break;
                case 'V':result+=5;
                    break;
                case  'X':result+=10;
                    break;
                case 'L' :result+=50;
                    break;
                case 'C' :result+=100;
                    break;
                case 'D' :result+=500;
                    break;
                case 'M' :result+=1000;                  
                    break;          
                default:
                    break;
            }
        }
        return result;
    }
}