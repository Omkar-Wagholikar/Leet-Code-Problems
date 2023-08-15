// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:

    bool checkPossibleDays(vector<int>& weights, int wt, int days){
        int d =1, cwt = 0;
        for(int i=0; i<weights.size(); i++){
            cwt += weights[i];
            if(cwt > wt){
                cwt = weights[i];
                d +=1;
                if(d > days){
                    return false;
                }
            }
        }
        return true;
    }

    int shipWithinDays(vector<int>& weights, int days) {
        int size = weights.size();
        int low = weights[0], high = 0, mid;
        bool poss;

        for(int a: weights){
            low = max(low, a);
            high += a;
        }


        while(low < high){
            mid = (high + low) /2;
            // cout<<low<<" "<<mid<<" "<<high<<endl;
            // check if mid amount of weight is possible;
            poss = checkPossibleDays(weights, mid, days);
            if(poss){
                high = mid;
            }
            else {
                low = mid+1;
            }
        }
        // cout<<low<<endl;
        return low;
    }
};

int main(){
    Solution a;

    // vector<int> weights = {147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47} ;
    // int days = 10;
    vector<int> weights = {3, 2, 2, 4, 1, 4} ;
    int days = 3;
    a.shipWithinDays(weights, days);
    return 0;
}