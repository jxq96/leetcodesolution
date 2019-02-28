public class GrayCode{
    public List<Integer> grayCode(int n) {
        ArrayList<Integer> res = new ArrayList<>();
int[] tmp = new int[n];
int i = 1;
res.add(0);
int bound = (int)Math.pow(2,n);
int t = 0;
while(i<bound){
    if(i%2==1) {
        if (tmp[n - 1] == 0) {
            t = t + 1;
            tmp[n - 1] = 1;
            res.add(t);
            i++;
        } else {
            t = t - 1;
            tmp[n - 1] = 0;
            res.add(t);
            i++;
        }
    }
    else{
        int j = n - 1;
        while(j>=0){
            if(tmp[j]==1){
                break;
            }
            j --;
        }
        if(j!=0){
            if(tmp[j-1]==1){
                t = t - (int)Math.pow(2,n-j);
                tmp[j-1] = 0;
                res.add(t);
                i++;
            }
            else{
                t = t + (int)Math.pow(2,n-j);
                tmp[j-1] = 1;
                res.add(t);
                i++;
            }
        }
    }
}
return res;
}
}