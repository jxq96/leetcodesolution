#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int sumCost,sumGas;
        for(int i = 0;i<gas.size();i++){
            sumCost = 0;
            sumGas = 0;
            for(int j = 0;j<gas.size();j++){
                sumGas += gas[(i+j)%gas.size()];
                sumCost += cost[(i+j)%gas.size()];
                if(sumCost>sumGas){
                    break;
                }
                if(j==gas.size()-1){
                    return i;
                }
            }
        }
        return -1;
    }
};