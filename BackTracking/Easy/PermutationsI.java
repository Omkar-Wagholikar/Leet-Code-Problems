import java.util.*;
import java.util.stream.Collectors;

public class PermutationsI {
    public static List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> finVal = new ArrayList<>();
        List<Integer> list = Arrays.stream(nums).boxed().collect(Collectors.toList());

        addRep(list, 0, finVal, true);
        return finVal;
    }

    public static void addRep(List<Integer> numbers, int start, List<List<Integer>> finVal, boolean firstPush){
        if(start>=numbers.size())return;
        
        int swp = numbers.get(start);
        if(firstPush == true){
            finVal.add(new ArrayList<>(numbers));
        }

        for(int i=start; i<numbers.size(); i++){
            List<Integer> copy = new ArrayList<>(numbers);

            copy.set(start, copy.get(i));
            copy.set(i, swp);

            if(i==start){
                addRep(copy, start+1, finVal, false);
            }else {
                addRep(copy, start+1, finVal, true);
            }

            copy.set(i, copy.get(start));
            copy.set(start, swp);
        }
    }
    public static void main(String [] args){
        int[] nums = new int[] {1, 2, 3, 4};
        permute(nums);
    }
}