#include <vector>
#include <iostream>
#include <numeric>
using namespace std;
class Solution {
public:
    int candy(vector<int>& ratings) {
        if(ratings.empty()){
            return 0;
        }
        else if(ratings.size()==1){
            return 1;
        }
        else{
            int candies[ratings.size()];
            if(ratings[0]>ratings[1]){
                candies[0] = 2;
            }
            else{
                candies[0] = 1;
            }
            for(int i = 1;i<ratings.size()-1;i++){
                if(ratings[i]<=ratings[i-1]){
                    if(ratings[i]<=ratings[i+1]){
                        candies[i] = 1;
                    }
                    else{
                        candies[i] = 2;
                    }
                }
                else{
                    candies[i] = candies[i-1] + 1;
                }
            }
            if(ratings[ratings.size()-1]>ratings[ratings.size()-2]){
                candies[ratings.size()-1] = candies[ratings.size()-2]+1;
            }
            else{
                candies[ratings.size()-1] = 1;
            }
            for(int i = ratings.size()-2;i>0;i--){
                if(ratings[i]>ratings[i+1]){
                    candies[i] = max(candies[i],candies[i+1]+1);
                }
            }
            if(ratings[0]>ratings[1]){
                candies[0] = max(candies[0],candies[1]+1);
            }
            int sum = 0;
            for(int i : candies){
                sum += i;
            }
            return sum;
        }
    }
};