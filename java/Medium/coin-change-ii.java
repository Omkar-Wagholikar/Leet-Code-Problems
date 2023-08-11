// https://leetcode.com/problems/coin-change-ii/
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int change(int amount, int[] coins) {
        Arrays.sort(coins);
        int [] row = new int[amount+1];
        row[0] =1;
        for(int a = coins.length-1; a>=0; a--)
        {
            int c = coins[a];
            for(int i=1; i<amount+1; i++){
                if(i - c >= 0){
                    row[i] = row[i] + row[i - c];
                }
            }
        }
        return row[amount];
    }
}

// public class Testing{
//     public static void main(String [] atgs){
//         Solution a = new Solution();
//         int coins[] = new int[]{1,2,5};
//         int amount =5;
//         System.out.println(a.change(amount, coins));
//     }
// }