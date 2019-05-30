#include <vector>
#include <iostream>
#include <numeric>
#include <string>
#include <cstring>
using namespace std;
class Solution {
public:
    int numDistinct(string s, string t) {
        if(s.size()<t.size()){
            return 0;
        }
        else {
            long long dp[s.size() + 1][t.size() + 1];
            for (int i = 0; i <= t.size(); i++) {
                dp[0][i] = 0;
            }
            for (int i = 0; i <= s.size(); i++) {
                dp[i][0] = 1;
            }
            for (int i = 1; i <= s.size(); i++) {
                for (int j = 1; j <= i && j <= t.size(); j++) {
                    if (i == j) {
                        if (s.substr(0, i) == t.substr(0, j)) {
                            dp[i][j] = 1;
                        } else {
                            dp[i][j] = 0;
                        }
                    } else {
                        if (s[i - 1] == t[j - 1]) {
                            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
                        } else {
                            dp[i][j] = dp[i - 1][j];
                        }
                    }
                }
            }
            return dp[s.size()][t.size()];
        }
    }
};

int main(){
    Solution s = Solution();
    string str = "babgbag";
    string t = "bag";
    cout << s.numDistinct(str,t);
}