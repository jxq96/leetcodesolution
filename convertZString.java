public class convertZString{
    public  String convert(String s,int numRows){
        int length = s.length();
        if(s==null||numRows==1||numRows>=length){
            return s;
        }
        StringBuffer answerString = new StringBuffer();
        for(int i = 1;i<length+1;i+=2*(numRows-1)){
            answerString.append(s.charAt(i-1));
        } //first row

        for(int i = 2;i<numRows;i++){
            boolean flag = true;
            for(int j = i;j<length+1;j+=(flag)?2*(numRows-i):2*(i-1),flag=!flag){
                 answerString.append(s.charAt(j-1));
            }
        }

        for(int i =numRows;i<length+1;i+=2*(numRows-1)){
            answerString.append(s.charAt(i-1));
        }
        return answerString.toString();
    }
}