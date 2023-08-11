// https://leetcode.com/problems/coin-change/description/
class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] cache = new int[amount+1];
        for(int ca=1; ca<=amount; ca++){
            cache[ca] = amount+1;
            for(int co: coins){
                if(ca-co >=0){
                    cache[ca] = Math.min(cache[ca], 1 + cache[ca-co]);
                }
            }
        }
        if(cache[amount] != amount+1){
            return cache[amount];
        }
        for(int c:cache){
            System.out.print(c + " ");
        }
        System.out.print(" H W ");
        return -1;
    }
}

// public class Testing{
//     public static void main(String [] atgs){
//         Solution a = new Solution();
//         int coins[] = new int[]{1,2,5};
//         int amount =11;
//         System.out.println("?");
//         a.coinChange(coins, amount);
//     }
// }