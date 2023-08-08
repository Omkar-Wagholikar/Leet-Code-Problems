// https://leetcode.com/problems/add-two-numbers

// Definition for singly-linked list.
class ListNode {
    public int val;
    public ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode va = l1;
        ListNode vb = l2;
        ListNode sum = new ListNode((va.val + vb.val) % 10);
        int carry = Math.floorDiv(va.val + vb.val, 10);
        ListNode temp = sum;
        va = va.next;
        vb = vb.next;

        while(va != null && vb != null){
            int s = va.val + vb.val;
            temp.next = new ListNode((s + carry) % 10);
            carry = Math.floorDiv(s + carry,  10);
            
            temp = temp.next;
            va = va.next;
            vb = vb.next;
        }

        if(vb != null) va = vb;

        while(va != null){
            int s = va.val + carry;
            temp.next = new ListNode(s%10);
            temp = temp.next;
            carry = Math.floorDiv(s, 10);
            va = va.next;
        }
        if(carry != 0){
            temp.next = new ListNode(carry);
        }
        return sum;
    }

    // public static void main(String [] args){
        
    //     int[] v2 = new int[]     {3, 7};
    //     int[] values = new int[] {9, 2};

    //     ListNode root1 = new ListNode(v2[0]);
    //     ListNode t = root1;
    //     for(int i=1; i<v2.length; i++){
    //         t.next = new ListNode(v2[i]);
    //         t= t.next;
    //     }

        

    //     ListNode root2 = new ListNode(values[0]);
    //     ListNode temp = root2;
    //     for(int i=1; i<values.length; i++){
    //         temp.next = new ListNode(values[i]);
    //         temp = temp.next;
    //     }
        
        
    //     ListNode sum = addTwoNumbers(root1, root2);
    //     while(sum != null){
    //         System.out.print(sum.val + " ");
    //         sum = sum.next;
    //     }
    // }
}