// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
class Solution {
    public int smallestDivisor(int[] nums, int threshold) {
        int high = nums[0], low = 1, mid=-12, divi=0;
        for(int n:nums) high = Math.max(high, n);
        while(low<high){
            System.out.print(low + " " + high + " " );
            mid = (high + low) / 2;
            divi = getDivisor(nums, mid);
            if(divi > threshold){
                low = mid+1;
            } else {
                high = mid;
            }
            System.out.println(mid + " " + divi + " > " + threshold);
            // if(low == mid) break;
        }
        System.out.println(low + " "+ high + " " + mid);
        return high;
    }
    public int getDivisor(int [] nums, int divisior){
        int total=0;
        for(int n:nums) total += (int) Math.ceil((double)n / divisior);
        return total;
    }
}


// public class Testing{
//     public static void main(String [] args){
//         Solution a = new Solution();
//         int [] nums = new int[]{19};
//         int threshold = 5;
//         System.out.println("_>"+a.smallestDivisor(nums, threshold));        
//         // System.out.println(a.getDivisor(nums, 4));
//     }
// }