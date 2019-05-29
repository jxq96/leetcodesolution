#include <vector>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy,sell;
        bool flag = false; // 当前是否持有股票
        int sum = 0;
        for(int i = 0;i<prices.size();i++){
            if(i==prices.size()-1){
                if(flag){
                    sum += prices[prices.size()-1] - prices[buy];
                }
            }
            else{
                if(prices[i]<prices[i+1]){
                    if(!flag){
                        buy = i;
                        flag = true;
                    }
                }
                else if(prices[i]>prices[i+1]){
                    if(flag){
                        sum += prices[i] - prices[buy];
                        flag = false;
                    }
                }

            }
        }
        return sum;
    }
};