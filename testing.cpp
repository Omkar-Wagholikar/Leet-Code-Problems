#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int shipWithinDays(vector<int>& weights, int days) {
        int size = weights.size();
        int minWt = 0, temp, prev =0;
        for(int i=1; i<size; i++){
            weights[i] += weights[i-1];
        }
        int quanta = weights[size-1] / days;
        for(int i=0; i<days; i++){
            temp = bisect_right(weights, quanta * (1 + i), size);
            if(weights[temp-1] == quanta * (i+1)) temp -=1;
            minWt = max(weights[temp] - prev, minWt);
            prev = weights[temp];
        }
        return minWt;
    }

    int bisect_right(vector<int>& weights, int day, int size){
        int low = 0, high = size, mid;
        while(low < high){
            mid = (low + high)/2;
            if(weights[mid] > day) high = mid;
            else low+=1;
        }
        return low;
    }
};

int main(){
    Solution a;
    vector<int> weights = {3, 2, 2, 4, 1, 4} ;
    int days = 3;
    cout<<a.shipWithinDays(weights, days);
    return 0;
}