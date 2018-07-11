public class numMagicSquaresInsideSolu{
    public int numMagicSquaresInside(int[][] grid) {
        int r = grid.length-1;
        int c = grid[0].length-1;
        int r1 = r+1;
        int c1 = c+1;
        int count = 0;
        for(int i = 1;i < r;i++){
            for(int j = 1;j < c;j++){
                if(i+1<r1&&j+1<c1){
                    int A = grid[i-1][j-1];
                    if(!(A>=1&&A<=9)){
                        continue;
                    }
                    int B =grid[i-1][j];
                    if(!(B>=1&&B<=9)){
                        j++;
                        continue;
                    }
                    int C = grid[i-1][j+1];
                    if(!(C>=1&&C<=9)){
                        j+=2;
                        continue;
                    }
                    int D = grid[i][j-1];
                    if(!(D>=1&&D<=9)){
                        continue;
                    }
                    int E = grid[i][j];
                    if(!(E>=1&&E<=9)){
                        j++;
                        continue;
                    }
                    int F = grid[i][j+1];
                    if(!(F>=1&&F<=9)){
                        j+=2;
                        continue;
                    }
                    int G = grid[i+1][j-1];
                    if(!(G>=1&&G<=9)){
                        continue;
                    }
                    int H = grid[i+1][j];
                    if(!(H>=1&&H<=9)){
                        j+=1;
                        continue;
                    }
                    int I = grid[i+1][j+1];
                    if(!(I>=1&&I<=9)){
                        j+=2;
                        continue;
                    }
                    int sum = E+D+F;
                    if(A+B+C==sum
                       && G+H+I==sum
                       && A+E+I==sum
                       && C+E+G==sum
                       && A+D+G==sum
                       && B+E+H==sum
                       && C+F+I==sum){
                           count++;
                       }
                }
            }
        }
        return count;
    }
}