public class intToRomeSolu{
    public String intToRoman(int num) {
        int thousand = num/1000;
        StringBuilder result = new StringBuilder();
        for(int i = 0 ;i < thousand;i++){
            result.append('M');
        }    
        num%=1000;
        int hundred =num/100;
        switch (hundred) {
            case 9: result.append("CM");
                break;
            case 8: result.append("DCCC");
                break;
            case 7: result.append("DCC");
                break;
            case 6: result.append("DC");
                break;
            case 5: result.append('D');
                break;
            case 4: result.append("CD");
                break;
            case 3: result.append("CCC");
                break;
            case 2: result.append("CC");
                break;
            case 1: result.append("C");
                break;    
            default:
                break;
        }   
        num%=100;
        int ten = num/10;
        switch (ten) {
            case 9: result.append("XC");
                break;
            case 8: result.append("LXXX");
                break;
            case 7: result.append("LXX");
                break;
            case 6: result.append("LX");
                break;
            case 5: result.append('L');
                break;
            case 4: result.append("XL");
                break;
            case 3: result.append("XXX");
                break;
            case 2: result.append("XX");
                break;
            case 1: result.append("X");                
                break;
            default:
                break;
        }
        num%=10;
        switch (num) {
            case 9: result.append("IX");
                break;
            case 8: result.append("VIII");
                break;
            case 7: result.append("VII");
                break;
            case 6: result.append("VI");
                break;
            case 5: result.append("V");
                break;
            case 4: result.append("IV");
                break;
            case 3: result.append("III");
                break;
            case 2: result.append("II");
                break;
            case 1: result.append('I');
                break;
            default:
                break;
        }
        return result.toString();
    }
}