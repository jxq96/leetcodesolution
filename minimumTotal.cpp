#include<vector>
#include<cstdio>
using namespace std;

int minimumTotal(vector<vector<int>>& triangle) {
        int rowCount = triangle.size();
        if(rowCount == 0){
            return 0;
        }
        else{
        int table[2][rowCount];
        table[0][0] = triangle[0][0];
        int k,l;
        for(int i = 1;i < rowCount;i++){
            k = i % 2;
            l = 1 - k;
            for(int j = 0; j <=i;j++){
                if(j==0){
                    table[k][j] = table[l][j] + triangle[i][j];
                }
                else if(j == i){
                    table[k][j] = table[l][j-1] + triangle[i][j];
                }
                else{
                    table[k][j] = min(table[l][j-1],table[l][j]) + triangle[i][j];
                }
            }
        }
        int minist = __INT32_MAX__;
        k = 1 - (rowCount % 2);
        for(int i = 0;i<rowCount;i++){
            if(table[k][i]<minist){
                minist = table[k][i];
            }
        }
        return minist;
        }
    }

    int main(){
        vector<vector<int>> test = {
            {-1},
            {2,3},
            {1,-1,-3}
        };
        printf("%d\n",minimumTotal(test));
    }