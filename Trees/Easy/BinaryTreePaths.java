package Trees;
// https://leetcode.com/problems/binary-tree-paths/description/
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class BinaryTreePaths {
    static List<String> fin = new ArrayList<>();

    public static List<String> binaryTreePaths(TreeNode root) {
        String t = "" + root.val;
        inorder(root.left, t);
        inorder(root.right, t);
        return fin;
    }

    static void inorder(TreeNode r, String tempPath){
        if(r != null){
            tempPath = tempPath + "->" + r.val;
            inorder(r.left,  tempPath);
            inorder(r.right, tempPath);
            if(r.right == null && r.left == null){
                fin.add(tempPath);
            }
        }
    }
    public static void main(String [] args){
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.left.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.right = new TreeNode(5);
        System.out.println(binaryTreePaths(root));
    }
}
