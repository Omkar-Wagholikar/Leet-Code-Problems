import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> tri = new ArrayList<List<Integer>>(numRows);
        for(List<Integer> a: tri){
            System.out.println(a);
        }
        return null;
    }
}
public class Testing{
    public static void main(String [] args){
        Solution a = new Solution();
        a.generate(2);
        // System.out.println()
    }
}