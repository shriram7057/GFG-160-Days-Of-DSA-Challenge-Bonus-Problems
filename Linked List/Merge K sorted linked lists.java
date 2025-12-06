/*
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}
*/
import java.util.*;
class Solution {
    Node mergeKLists(Node[] arr) {
        // code here
        PriorityQueue<Node> pq= new PriorityQueue<>(
            (a,b) -> a.data-b.data
            );
        for(Node node : arr){
            if (node != null)
                pq.add(node);
        }
        Node dummy = new Node(0);
        Node tail = dummy;
        
        while(!pq.isEmpty())
        {
            Node node = pq.poll();
            tail.next=node;
            tail = tail.next;
            
            if (node.next != null)
            {
                pq.add(node.next);
            }
        }
        return dummy.next;
    }
}