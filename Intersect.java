// Find out of two linkedlist intersect at some point

// Naive solution: throw all the links into a hash and then return true
// when there is a match
public class Intersect {
    public boolean intersection(Linkedlist l1, Linkedlist l2) {
        Hashtable hash = new Hashtable();
        Node node1 = l1.head;
        Node node2 = l2.head;
        // This assumes that there is no loop
        while (node1 || node2) {

            // If the current node is already in the hash,
            // then it has already been visited, and therefore,
            // there must be an intersection

            if (hash.get(node1) || hash.get(node2)) {
                return true;
            }

            // just in case one is still running while the other is null
            node1 = node1 != null ? node1.next : null;
            node2 = node2 != null ? node2.next : null;
        }
        return false;
    }
}
